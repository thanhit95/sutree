from .tree_base import print_bin_tree
from sutree import AvlTree


def do_task():
    avl = AvlTree()

    for value in [10, 20, 30, 40, 50, 25]:
        avl.insert(value)

    print('\n size:', avl.size())
    print('\n min:', avl.min())
    print('\n max:', avl.max())
    print('\n contain:', avl.contain(50))
    print('\n height:', avl.height())

    print('\n print tree')
    print_bin_tree(avl)

    print()
