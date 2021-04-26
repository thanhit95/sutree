from .abtreedisplay import AbstractTreeDisplay
from .valueutil import ValueUtil
from .matrixbuffer import MatrixBuffer
from .parsingnode import ParsingNode
from .bintreeparser import BinTreeParser


#
#
class BinTreeDisplay(AbstractTreeDisplay):
    '''
    A utility help visualize binary trees by using ASCII text.
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
        self._parser = BinTreeParser(self._vutil)
        self.config(compact_vert_line=True)

    #
    #
    def config(self, **kwargs):
        '''
        Configures settings.

        Args:
            struct_node: Tuple(name_key, name_left, name_right) indicating structure information of input node.

            space_branch_neighbor: Space between 2 branch neighbors.

            float_pre: Maximum precision of floating-point numbers.

            leaf_at_bottom: True if leaf will be drawn at bottom. Otherwise, False.

            compact_vert_line: True if vertical dash below will be omitted. Otherwise, False.

            margin_left: Left margin of output string result.

            hori_line_char: Display character for the horizontal line connecting branches.
        '''
        super()._config(kwargs)

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

        self._buffer.fill_str(node.margin_key, y_depth, node.key)
        self._buffer.fill_str(node.margin_key_center, y_depth + 1, '|')
        self._buffer.fill_hori_line(self._hori_line_char, y_depth + 2, node.hori_line_xstart, node.hori_line_xend)

        y_depth += 3

        # vertical dash below
        if node.le is not None and not self._compact_vert_line:
            self._buffer.fill_str(node.margin_vert_dash_below_le, y_depth, '|')

        if node.ri is not None and not self._compact_vert_line:
            self._buffer.fill_str(node.margin_vert_dash_below_ri, y_depth, '|')

        if not self._compact_vert_line:
            y_depth += 1

        # process children
        if node.le is not None:
            self._fill_buffer(node.le, y_depth)

        if node.ri is not None:
            self._fill_buffer(node.ri, y_depth)

    #
    #
    def _get_height_buffer(self, height_inp_root: int) -> int:
        if self._compact_vert_line:
            return height_inp_root * 3 - 2

        return height_inp_root * 4 - 3
