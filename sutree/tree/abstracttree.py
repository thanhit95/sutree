'''

ABSTRACT TREE

Description:    Abstract base class of a tree

'''


import copy
from abc import ABC, abstractmethod


#
#
class AbstractTree(ABC):
    '''
    Abstract base class of a tree.
    '''
    #################################################################
    #                        ABSTRACT METHODS
    #################################################################
    #
    #
    def __init__(self):
        self._root = None

    #
    #
    @abstractmethod
    def empty(self):
        raise NotImplementedError()

    #
    #
    @abstractmethod
    def size(self):
        raise NotImplementedError()

    #
    #
    @abstractmethod
    def height(self):
        raise NotImplementedError()

    #
    #
    @abstractmethod
    def clear(self):
        raise NotImplementedError()

    #
    #
    @abstractmethod
    def traverse(self, order: str = 'in') -> list:
        raise NotImplementedError()

    #
    #
    @abstractmethod
    def insert(self, key):
        raise NotImplementedError()

    #
    #
    @abstractmethod
    def remove(self, key):
        raise NotImplementedError()

    #
    #
    #################################################################
    #                        METHODS (PUBLIC)
    #################################################################
    #
    #
    def clone(self):
        '''
        Clones tree completely.
        '''
        the_clone = copy.deepcopy(self)
        return the_clone

    #
    #
    #################################################################
    #                        METHODS (EXTRA)
    #################################################################
    #
    #
    def _get_traversal_str(self) -> str:
        lst_traversal = self.traverse('in')
        res = '  '.join(str(x) for x in lst_traversal)
        res = f'({res})'
        return res

    #
    #
    def __str__(self) -> str:
        return self._get_traversal_str()
