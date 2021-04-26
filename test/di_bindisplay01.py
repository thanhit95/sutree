from sutree import BinTreeDisplay


class Node:
    def __init__(self, key):
        self.key = key
        self.le = None
        self.ri = None


def create_tree():
    a = Node('abcde')
    b = Node('ok')
    c = Node('keo')
    d = Node(123)

    a.le = b
    a.ri = c
    c.le = d

    return a


def do_task():
    disp = BinTreeDisplay()
    tree = create_tree()

    disp.config(
        struct_node=('key', 'le', 'ri'),
        leaf_at_bottom=False,
        space_branch_neighbor=2
    )

    res = disp.get(tree)
    print(res)
