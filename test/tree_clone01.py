from .tree_base import display_bin_tree
from sutree import AvlTree


def do_task():
    a = AvlTree()

    for value in [10, 20, 30, 40, 50, 25, 100, 28, 140]:
        a.insert(value)

    print(' display tree a:')
    display_bin_tree(a)

    ###########################################

    b = a.clone()
    b.insert(22)
    b.insert(29)
    print('\n\n\n display tree b:')
    display_bin_tree(b)
    print('\n\n height tree b:', b.height())

    ###########################################

    print('\n\n\n display tree a (again):')
    display_bin_tree(a)

    ###########################################

    c = a.clone()
    c.clear()
    print('\n\n\n display tree c:')
    display_bin_tree(c)

    print()
