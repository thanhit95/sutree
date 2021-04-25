from .parsingnode import ParsingNode
from .valueutil import ValueUtil


#
#
class BinTreeParser:
    #
    #
    def __init__(self, value_util: ValueUtil):
        if value_util is None:
            raise ValueError('value_util cannot be None')

        self.vutil = value_util
        self.config(struct_node=('key', 'left', 'right'), space_branch_neighbor=1)

    #
    #
    def config(self, **kwargs):
        '''
        Configures settings.

        Args:
            struct_node: Tuple(name_key, name_left, name_right) indicating structure information of input node.

            space_branch_neighbor: Space between 2 branch neighbors.
        '''
        for arg, argval in kwargs.items():
            if arg == 'struct_node':
                if type(argval) is not tuple or len(argval) != 3 \
                        or type(argval[0]) is not str or type(argval[1]) is not str or type(argval[2]) is not str:
                    raise ValueError('Invalid argument: struct_node must be a tuple(name_key, name_left, name_right)')

                self.struct_node_key = argval[0]
                self.struct_node_le = argval[1]
                self.struct_node_ri = argval[2]

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
        input_le = getattr(input_root, self.struct_node_le)
        input_ri = getattr(input_root, self.struct_node_ri)

        node = ParsingNode(self.vutil.get_str(input_key))

        # STEP 1. Children tree processing
        node.le = self.build_tree(input_le)
        node.ri = self.build_tree(input_ri)

        # STEP 2. Common factors
        has_child_le = node.le is not None
        has_child_ri = node.ri is not None
        is_leaf = not has_child_le and not has_child_ri

        width_child_le = node.le.width if has_child_le else 0
        width_child_ri = node.ri.width if has_child_ri else 0

        # magic adjustment ==> the most left child
        if has_child_le:
            tmp = len(node.le.key)
            if tmp > 0 and tmp % 2 == 0:
                node.le.margin_key_center += 1

        margin_child_ri = width_child_le + self.space_branch_neighbor

        margin_vert_dash_below_le = node.le.margin_key_center if has_child_le else -1
        margin_vert_dash_below_ri = margin_child_ri + (node.ri.margin_key_center if has_child_ri else 0)

        # STEP 3. Horizontal line
        hori_line_xstart, hori_line_xend = None, None

        if not is_leaf:
            hori_line_xstart = margin_vert_dash_below_le + 1
            hori_line_xend = margin_vert_dash_below_ri - 1

        # STEP 4. Margin of current node
        margin_key_center = tmp = max(0, len(node.key) - 1) // 2

        if not is_leaf:
            if has_child_le and has_child_ri:
                margin_key_center = (hori_line_xstart + hori_line_xend) // 2
            elif has_child_le:
                margin_key_center = hori_line_xend
            elif has_child_ri:
                margin_key_center = 0

        margin_key = margin_key_center - tmp

        # STEP 5. Width of current node
        width_chbrsp = margin_child_ri + width_child_ri if not is_leaf else 0
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
            node.margin_vert_dash_below_le = margin_vert_dash_below_le
            node.margin_vert_dash_below_ri = margin_vert_dash_below_ri
            node.margin_child_le = 0
            node.margin_child_ri = margin_child_ri

        self.adjust_margin_key(node)

        del input_key
        del input_le
        del input_ri
        del has_child_le
        del has_child_ri
        del is_leaf
        del width_child_le
        del width_child_ri
        del margin_child_ri
        del margin_vert_dash_below_le
        del margin_vert_dash_below_ri
        del hori_line_xstart
        del hori_line_xend
        del margin_key_center
        del margin_key
        del width_chbrsp
        del full_width
        del tmp

        return node

    #
    #
    def adjust_margin_key(self, node: ParsingNode):
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

        if node.le is not None:
            self.convert_margin_local_to_global(node.le, node.margin_child_le)

        if node.ri is not None:
            self.convert_margin_local_to_global(node.ri, node.margin_child_ri)

    #
    #
    def shift_margin_except_children(self, node: ParsingNode, shift_factor: int):
        node.margin_key += shift_factor
        node.margin_key_center += shift_factor

        if not node.is_leaf:
            node.hori_line_xstart += shift_factor
            node.hori_line_xend += shift_factor
            node.margin_vert_dash_below_le += shift_factor
            node.margin_vert_dash_below_ri += shift_factor
            node.margin_child_le += shift_factor
            node.margin_child_ri += shift_factor

    #
    #
    def destroy_tree(self, node: ParsingNode):
        if node is None:
            return

        self.destroy_tree(node.le)
        del node.le

        self.destroy_tree(node.ri)
        del node.ri

        del node.key
        del node.width
        del node.margin_key
        del node.margin_key_center

        if not node.is_leaf:
            del node.width_chbrsp
            del node.hori_line_xstart
            del node.hori_line_xend
            del node.margin_vert_dash_below_le
            del node.margin_vert_dash_below_ri
            del node.margin_child_le
            del node.margin_child_ri

        del node.is_leaf

    #
    #
    def get_height(self, node) -> int:
        if node is None:
            return 0

        height_le = self.get_height(getattr(node, self.struct_node_le))
        height_ri = self.get_height(getattr(node, self.struct_node_ri))

        return 1 + max(height_le, height_ri)
