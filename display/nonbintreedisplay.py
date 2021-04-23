'''

NON-BINARY TREE DISPLAY

Description:    A utility help visualize non-binary trees by using ASCII text.

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        3-Clause BSD License

'''


from enum import Enum
from .valueutil import ValueUtil
from .matrixbuffer import MatrixBuffer
from .parsingnode import ParsingNode
from .nonbintreeparser import NonBinTreeParser


#
#
class FillDirection(Enum):
    LEFT = 0
    RIGHT = 1


#
#
class NonBinTreeDisplay:
    '''
    Binary tree display. A utility help visualize binary trees by using ASCII text.
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
        self._parser = NonBinTreeParser(self._vutil)
        self._buffer = None
        self.config(leaf_at_bottom=False, hori_line_char='-', margin_left=0)

    #
    #
    def get(self, inp_root) -> str:
        '''
        Gets display string for binary search tree.
        Output result can be configured by calling "config" method. Configurable properties are:
            struct_node, line_char, line_brsp, margin_left, float_pre
        Args:
            inp_root: Input root of binary search tree.
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
        Gets display string for binary search tree.
        Output result can be configured by calling "config" method. Configurable properties are:
            struct_node, line_char, line_brsp, margin_left, float_pre
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
            struct_node: Tuple(name_key, name_lst_children) indicating structure information of input node.
            space_branch_neighbor: Space between 2 branch neighbors.
            float_pre: Maximum precision of floating-point numbers when displays.
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
        self._fill_buffer(parsing_tree, 1)

        self._parser.destroy_tree(parsing_tree)

    #
    #
    def _fill_buffer(self, node: ParsingNode, depth: int):
        if node is None:
            return

        if node.is_leaf:
            self._fill_buffer_node_leaf(node, depth)
            return

        num_children = len(node.children)

        self._buffer.fill_str(node.margin_key, depth * 4 - 4, node.key)
        self._buffer.fill_str(node.margin_key_center, depth * 4 - 3, '|')

        hori_line_char = self._hori_line_char if num_children > 1 else '|'
        self._buffer.fill_hori_line(hori_line_char, depth * 4 - 2, node.hori_line_xstart, node.hori_line_xend)

        vert_dash_below_char = '|'

        for i in range(num_children):
            vert_dash_below_char = '|'

            if i == 0 and num_children >= 2:
                vert_dash_below_char = '/'
            elif i == num_children - 1 and num_children >= 2:
                vert_dash_below_char = '\\'

            self._buffer.fill_str(node.margin_vert_dash_below[i], depth * 4 - 1, vert_dash_below_char)
            self._fill_buffer(node.children[i], depth + 1)

    #
    #
    def _fill_buffer_node_leaf(self, node: ParsingNode, depth: int):
        y_end = y_start = depth * 4 - 4

        if self._leaf_at_bottom:
            y_end = self._buffer.height() - 1
            self._buffer.fill_vert_line('|', node.margin_key_center, y_start, y_end - 1)

        self._buffer.fill_str(node.margin_key, y_end, node.key)
