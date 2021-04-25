from pytreedisplay import NonBinTreeDisplay


class Node:
    def __init__(self, key):
        self.key = key
        self.children = []


def create_tree():
    a = Node('ConChimDangChoiCo')
    b = Node('dog')
    c = Node('abcdefghi')
    d = Node('s')
    e = Node(-123)
    f = Node(8)

    a.children.append(b)
    a.children.append(c)
    a.children.append(d)

    c.children.append(e)
    c.children.append(f)

    return a


def do_task():
    tree = create_tree()
    disp = NonBinTreeDisplay()

    disp.config(
        leaf_at_bottom=False,
        space_branch_neighbor=1
    )

    res = disp.get(tree)
    print(res)
