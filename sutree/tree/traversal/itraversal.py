'''

TREE TRAVERSAL

Description:    Base class which help traverse through a tree.

'''


#
#
class ITraversal:
    def traverse(self, root, order: str) -> list:
        '''
        Traverses a tree entirely.
        Args:
            order: Type of traversal order.
                - 'pre': pre-order
                - 'in': in-order
                - 'post': post-order
        Returns:
            A list of keys.
        '''
        raise NotImplementedError()
