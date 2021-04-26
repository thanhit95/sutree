from sutree.display import BinTreeDisplay


#
#
def print_bin_tree(tree, order: str = 'in'):
    # print(tree)
    res = tree.traverse(order)
    print(res)


#
#
def display_bin_tree(tree):
    disp = BinTreeDisplay()

    disp.config(
        struct_node=('key', 'left', 'right')
    )

    res = tree.display(disp)
    print(res)

    del disp
