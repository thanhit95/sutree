from .valueutil import ValueUtil
from .matrixbuffer import MatrixBuffer
from .parsingnode import ParsingNode
from .bintreeparser import BinTreeParser
from .filldirection import FillDirection


#
#
class BinTreeDisplay:
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
        self._vutil = ValueUtil()
        self._parser = BinTreeParser(self._vutil)
        self._buffer = None
        self.config(leaf_at_bottom=False, hori_line_char='-', margin_left=0)

    #
    #
    def get(self, inp_root) -> str:
        '''
        Gets ASCII display string of tree. Output result is configurable by calling method "config".

        Args:
            inp_root: Input root of tree.

        Returns:
            String result. If inp_root is None then returns an empty string.
        '''
        if inp_root is None:
            return ''

        self._process(inp_root)
        assert self._buffer is not None

        res = self._buffer.get_str()

        del self._buffer
        return res

    #
    #
    def get_lst_rows(self, inp_root) -> list:
        '''
        Gets ASCII display string of tree. Output result is configurable by calling method "config".

        Args:
            inp_root: Input root of tree.

        Returns:
            List of rows. Each row is a string. If inp_root is None then returns an empty list.
        '''
        if inp_root is None:
            return []

        self._process(inp_root)
        assert self._buffer is not None

        res = self._buffer.get_lst_rows()

        del self._buffer
        return res

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
        for arg, argval in kwargs.items():
            if arg == 'struct_node':
                self._parser.config(struct_node=argval)

            elif arg == 'space_branch_neighbor':
                self._parser.config(space_branch_neighbor=argval)

            elif arg == 'float_pre':
                self._vutil.set_float_precision(argval)

            elif arg == 'leaf_at_bottom':
                if type(argval) is not bool:
                    raise ValueError('Invalid argument: leaf_at_bottom must be a boolean')

                self._leaf_at_bottom = argval

            elif arg == 'hori_line_char':
                if type(argval) is not str or len(argval) != 1:
                    raise ValueError('Invalid argument: hori_line_char must be a string of length 1')

                self._hori_line_char = argval

            elif arg == 'margin_left':
                if type(argval) is not int or argval < 0:
                    raise ValueError('Invalid argument: margin_left must be a non-negative integer')

                self._margin_left = argval

            else:
                raise ValueError('Invalid argument:', arg)

    #
    #
    #################################################################
    #                        METHODS (PROTECTED)
    #################################################################
    #
    #
    def _process(self, inp_root):
        '''
        Backend function for "get" method.
        '''
        height_inp_root = self._parser.get_height(inp_root)
        height_buffer = height_inp_root * 4 - 3

        parsing_tree = self._parser.build_tree(inp_root)
        self._parser.convert_margin_local_to_global(parsing_tree, self._margin_left)

        self._buffer = MatrixBuffer(parsing_tree.width, height_buffer)
        self._fill_buffer(parsing_tree, 0)

        self._parser.destroy_tree(parsing_tree)

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
    def _fill_buffer_node_leaf(self, node: ParsingNode, y_depth: int):
        y_depth_end = y_depth

        if self._leaf_at_bottom:
            y_depth_end = self._buffer.height() - 1
            self._buffer.fill_vert_line('|', node.margin_key_center, y_depth, y_depth_end - 1)

        self._buffer.fill_str(node.margin_key, y_depth_end, node.key)
