from .abtreedisplay import AbstractTreeDisplay
from .valueutil import ValueUtil
from .matrixbuffer import MatrixBuffer
from .parsingnode import ParsingNode
from .nonbintreeparser import NonBinTreeParser


#
#
class NonBinTreeDisplay(AbstractTreeDisplay):
    '''
    A utility help visualize non-binary trees by using ASCII text.
    '''
    #
    #
    #################################################################
    #                        METHODS (PUBLIC)
    #################################################################
    #
    #
    def __init__(self):
        super().__init__()
        self._parser = NonBinTreeParser(self._vutil)
        self.config(compact_single_leaf=True)

    #
    #
    def config(self, **kwargs):
        '''
        Configures settings.

        Args:
            struct_node: Tuple(name_key, name_lst_children) indicating structure information of input node.

            space_branch_neighbor: Space between 2 branch neighbors.

            float_pre: Maximum precision of floating-point numbers.

            leaf_at_bottom: True if leaf will be drawn at bottom. Otherwise, False.

            compact_vert_line: True if vertical dash below will be omitted. Otherwise, False.

            margin_left: Left margin of output string result.

            hori_line_char: Display character for the horizontal line connecting branches.

            compact_single_leaf: True, if node has only a single child then this child will be compact. Otherwise, False. This setting is disabled when leaf_at_bottom is True.
        '''
        super()._config(kwargs)

        #
        argval = kwargs.pop('compact_single_leaf', None)
        if argval is not None:
            if type(argval) is not bool:
                raise ValueError('Invalid argument: compact_single_leaf must be a boolean')

            self._compact_single_leaf = argval

        #
        if kwargs:
            args_invalid = list(kwargs.keys())
            raise ValueError('Invalid argument(s):', args_invalid)

    #
    #
    #################################################################
    #                        METHODS (PROTECTED)
    #################################################################
    #
    #
    def _fill_buffer(self, node: ParsingNode, y_depth: int):
        if node is None:
            return

        if node.is_leaf:
            self._fill_buffer_node_leaf(node, y_depth)
            return

        num_children = len(node.children)

        self._buffer.fill_str(node.margin_key, y_depth, node.key)
        self._buffer.fill_str(node.margin_key_center, y_depth + 1, '|')

        if num_children == 1 and not self._leaf_at_bottom and self._compact_single_leaf:
            self._buffer.fill_str(node.children[0].margin_key, y_depth + 2, node.children[0].key)
            return

        hori_line_char = self._hori_line_char if num_children > 1 else '|'
        self._buffer.fill_hori_line(hori_line_char, y_depth + 2, node.hori_line_xstart, node.hori_line_xend)

        y_depth += 3
        y_depth += 1 if not self._compact_vert_line else 0

        for i in range(num_children):
            if not self._compact_vert_line:
                self._buffer.fill_str(node.margin_vert_dash_below[i], y_depth - 1, '|')
            self._fill_buffer(node.children[i], y_depth)

    #
    #
    def _get_height_buffer(self, height_inp_root: int) -> int:
        if self._compact_vert_line:
            return height_inp_root * 3 - 2

        return height_inp_root * 4 - 3
