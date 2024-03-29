from .tree_base import display_bin_tree
from sutree import AvlTree


def do_task():
    avl = AvlTree(canddrm='left')

    for value in 'INFORMATIONTECHNOLOGY':
        print(f'\n\n\n\n insert {value} \n')
        avl.insert(value)
        display_bin_tree(avl)

    print()

    for value in 'ECI':
        print(f'\n\n\n\n remove {value} \n')
        avl.remove(value)
        display_bin_tree(avl)

    print()
