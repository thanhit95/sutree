from .parsingnode import ParsingNode
from .valueutil import ValueUtil


#
#
class NonBinTreeParser:
    #
    #
    def __init__(self, value_util: ValueUtil):
        if value_util is None:
            raise ValueError('value_util cannot be None')

        self.vutil = value_util
        self.config(struct_node=('key', 'children'), space_branch_neighbor=1)

    #
    #
    def config(self, **kwargs):
        '''
        Configures settings.

        Args:
            struct_node: Tuple(name_key, name_lst_children) indicating structure information of input node.

            space_branch_neighbor: Space between 2 branch neighbors.
        '''
        for arg, argval in kwargs.items():
            if arg == 'struct_node':
                if type(argval) is not tuple or len(argval) != 2 \
                        or type(argval[0]) is not str or type(argval[1]) is not str:
                    raise ValueError('Invalid argument: struct_node must be a tuple(name_key, name_children)')

                self.struct_node_key = argval[0]
                self.struct_node_children = argval[1]

            elif arg == 'space_branch_neighbor':
                if type(argval) is not int or argval < 1:
                    raise ValueError('Invalid argument: space_branch_neighbor must be a positive integer')

                self.space_branch_neighbor = argval

            else:
                raise ValueError('Invalid argument:', arg)

    #
    #
    def build_tree(self, input_root) -> ParsingNode:
        '''
        Builds parsing tree which stores parsing information of each corresponding node.
        The structure of input_root should be configured by method "config".

        Args:
            input_root: Input root node.

        Returns:
            A node of type ParsingNode indicating parsing tree.
        '''
        if input_root is None:
            return None

        input_key = getattr(input_root, self.struct_node_key)
        input_children = getattr(input_root, self.struct_node_children)

        node = ParsingNode(self.vutil.get_str(input_key))
        node.children = []

        # STEP 1. Children tree processing
        for input_child in input_children:
            if input_child is None:
                continue
            parsing_child_node = self.build_tree(input_child)
            node.children.append(parsing_child_node)

        children = node.children  # alias

        # STEP 2. Common factors
        num_children = len(children)
        is_leaf = (num_children == 0)

        width_children = [child.width for child in children]

        # magic adjustment ==> the most left child
        if num_children >= 2 and len(children[0].key) > 0 and len(children[0].key) % 2 == 0:
            children[0].margin_key_center += 1

        margin_prefix_children = self.get_margin_prefix_children(num_children, width_children)
        margin_vert_dash_below = self.get_margin_vert_dash_below(children, margin_prefix_children)

        # STEP 3. Horizontal line
        hori_line_xstart, hori_line_xend = None, None

        if num_children == 1:
            hori_line_xstart = hori_line_xend = margin_vert_dash_below[0]
        elif num_children > 1:
            hori_line_xstart = margin_vert_dash_below[0] + 1
            hori_line_xend = margin_vert_dash_below[-1] - 1

        # STEP 4. Margin of current node
        margin_key, margin_key_center = 0, 0

        if is_leaf:
            margin_key_center = max(0, len(node.key) - 1) // 2
        else:
            margin_key_center = (hori_line_xstart + hori_line_xend) // 2
            margin_key = margin_key_center - max(0, len(node.key) - 1) // 2

        # STEP 5. Width of current node
        width_chbrsp = margin_prefix_children[-1] + width_children[-1] if not is_leaf else 0
        full_width = width_chbrsp if not is_leaf else len(node.key)

        # FINAL STEP
        node.width = full_width
        node.margin_key = margin_key
        node.margin_key_center = margin_key_center
        node.is_leaf = is_leaf

        if not is_leaf:
            node.width_chbrsp = width_chbrsp  # width of children + branch spacing
            node.hori_line_xstart = hori_line_xstart
            node.hori_line_xend = hori_line_xend
            node.margin_vert_dash_below = margin_vert_dash_below
            node.margin_prefix_children = margin_prefix_children

        self.adjust_too_long_key(node)

        del input_key
        del input_children
        del children
        del num_children
        del is_leaf
        del width_children
        del margin_prefix_children
        del margin_vert_dash_below
        del hori_line_xstart
        del hori_line_xend
        del margin_key
        del margin_key_center
        del width_chbrsp
        del full_width

        return node

    #
    #
    def get_margin_prefix_children(self, num_children: int, width_children: list):
        a = [0] * num_children

        for i in range(1, num_children):
            a[i] = a[i - 1] + width_children[i - 1] + self.space_branch_neighbor

        return a

    #
    #
    def get_margin_vert_dash_below(self, lst_children: list, margin_prefix_children: list):
        a = []

        for i in range(len(lst_children)):
            a.append(lst_children[i].margin_key_center + margin_prefix_children[i])

        return a

    #
    #
    def adjust_too_long_key(self, node: ParsingNode):
        if node.margin_key >= 0 and node.margin_key + len(node.key) <= node.width:
            return

        shift_factor = 0 if node.margin_key >= 0 else abs(node.margin_key)

        if node.margin_key + len(node.key) > node.width:
            node.width = shift_factor + node.margin_key + len(node.key)

        self.shift_margin_except_children(node, shift_factor)

        del shift_factor

    #
    #
    def convert_margin_local_to_global(self, node: ParsingNode, shift_factor: int):
        self.shift_margin_except_children(node, shift_factor)

        for i in range(len(node.children)):
            child = node.children[i]
            child_shift_factor = node.margin_prefix_children[i]
            self.convert_margin_local_to_global(child, child_shift_factor)

    #
    #
    def shift_margin_except_children(self, node: ParsingNode, shift_factor: int):
        node.margin_key += shift_factor
        node.margin_key_center += shift_factor

        if not node.is_leaf:
            node.hori_line_xstart += shift_factor
            node.hori_line_xend += shift_factor
            node.margin_vert_dash_below = [value + shift_factor for value in node.margin_vert_dash_below]
            node.margin_prefix_children = [value + shift_factor for value in node.margin_prefix_children]

    #
    #
    def destroy_tree(self, node: ParsingNode):
        if node is None:
            return

        for child in node.children:
            self.destroy_tree(child)

        del node.key
        del node.children
        del node.width
        del node.margin_key
        del node.margin_key_center

        if not node.is_leaf:
            del node.width_chbrsp
            del node.hori_line_xstart
            del node.hori_line_xend
            del node.margin_vert_dash_below
            del node.margin_prefix_children

        del node.is_leaf

    #
    #
    def get_height(self, node) -> int:
        if node is None:
            return 0

        children = getattr(node, self.struct_node_children)
        max_height = 0

        for child in children:
            child_height = self.get_height(child)
            max_height = max(max_height, child_height)

        del children

        return 1 + max_height
