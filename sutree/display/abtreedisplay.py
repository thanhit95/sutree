from abc import ABC, abstractmethod
from .valueutil import ValueUtil
from .matrixbuffer import MatrixBuffer
from .parsingnode import ParsingNode


#
#
class AbstractTreeDisplay(ABC):
    '''
    Base class for tree display.
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
        self._parser = None
        self._buffer = None

        self._config(dict(
            leaf_at_bottom=False, compact_vert_line=False, margin_left=0, hori_line_char='-'
        ))

    #
    #
    def get(self, inp_root) -> str:
        '''
        Gets ASCII display string of tree. Output result is configurable by calling method "config".

        Args:
            inp_root: Input root of tree.

        Returns:
            String result. If inp_root is None, return an empty string.
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
            List of rows. Each row is a string. If inp_root is None, return an empty list.
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
    #################################################################
    #                        METHODS (PROTECTED)
    #################################################################
    #
    #
    def _config(self, kwargs):
        '''
        Configures settings:
            struct_node, space_branch_neighbor, float_pre, leaf_at_bottom,
            compact_vert_line, margin_left, hori_line_char
        '''
        #
        argval = kwargs.pop('struct_node', None)
        if argval is not None:
            self._parser.config(struct_node=argval)

        #
        argval = kwargs.pop('space_branch_neighbor', None)
        if argval is not None:
            self._parser.config(space_branch_neighbor=argval)

        #
        argval = kwargs.pop('float_pre', None)
        if argval is not None:
            self._vutil.set_float_precision(argval)

        #
        argval = kwargs.pop('leaf_at_bottom', None)
        if argval is not None:
            if type(argval) is not bool:
                raise ValueError('Invalid argument: leaf_at_bottom must be a boolean')

            self._leaf_at_bottom = argval

        #
        argval = kwargs.pop('compact_vert_line', None)
        if argval is not None:
            if type(argval) is not bool:
                raise ValueError('Invalid argument: compact_vert_line must be boolean')

            self._compact_vert_line = argval

        #
        argval = kwargs.pop('margin_left', None)
        if argval is not None:
            if type(argval) is not int or argval < 0:
                raise ValueError('Invalid argument: margin_left must be a non-negative integer')

            self._margin_left = argval

        #
        argval = kwargs.pop('hori_line_char', None)
        if argval is not None:
            if type(argval) is not str or len(argval) != 1:
                raise ValueError('Invalid argument: hori_line_char must be a string of length 1')

            self._hori_line_char = argval

    #
    #
    def _process(self, inp_root):
        '''
        Backend function for "get" method.
        '''
        if inp_root is None:
            raise ValueError('Cannot process an empty tree')

        height_inp_root = self._parser.get_height(inp_root)
        height_buffer = self._get_height_buffer(height_inp_root)

        parsing_tree = self._parser.build_tree(inp_root)
        self._parser.convert_margin_local_to_global(parsing_tree, self._margin_left)

        self._buffer = MatrixBuffer(parsing_tree.width + self._margin_left, height_buffer)
        self._fill_buffer(parsing_tree, 0)

        self._parser.destroy_tree(parsing_tree)

    #
    #
    def _fill_buffer_node_leaf(self, node: ParsingNode, y_depth: int):
        y_depth_end = y_depth

        if self._leaf_at_bottom:
            y_depth_end = self._buffer.height() - 1
            self._buffer.fill_vert_line('|', node.margin_key_center, y_depth, y_depth_end - 1)

        self._buffer.fill_str(node.margin_key, y_depth_end, node.key)

    #
    #
    @abstractmethod
    def _fill_buffer(self, node: ParsingNode, y_depth: int):
        raise NotImplementedError()

    #
    #
    @abstractmethod
    def _get_height_buffer(self, height_inp_root: int) -> int:
        raise NotImplementedError()
