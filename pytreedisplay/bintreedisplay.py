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

            hori_line_char: Display character for the horizontal line connecting branches.

            margin_left: Left margin of output string result.
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

        if node.le is not None:
            self._buffer.fill_str(node.margin_vert_dash_below_le, y_depth + 3, '/')
            self._fill_buffer(node.le, y_depth + 4)

        if node.ri is not None:
            self._buffer.fill_str(node.margin_vert_dash_below_ri, y_depth + 3, '\\')
            self._fill_buffer(node.ri, y_depth + 4)

    #
    #
    def _get_height_buffer(self, height_inp_root: int) -> int:
        return height_inp_root * 4 - 3
