from .tree_base import display_bin_tree
from sutree import BinSearchTree


def do_task():
    bst = BinSearchTree()

    for value in [12, 39, 20, 7, 26, 45, 19, 8]:
        bst.insert(value)

    print('\n display tree')
    display_bin_tree(bst)

    print('\n')

    for value in [12, 39, 20, 7, 26, 45, 19, 8]:
        bst.remove(value)

    print('\n display tree')
    display_bin_tree(bst)

    print()
