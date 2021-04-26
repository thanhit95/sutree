from sutree import BinTreeDisplay


class Node:
    def __init__(self, key):
        self.key = key
        self.le = None
        self.ri = None


def create_tree():
    a = Node(100)
    b = Node(50)
    c = Node(70000)
    d = Node(10)
    e = Node(88.523816)
    f = Node(20000)
    g = Node(90000)
    h = Node(-123456)
    i = Node(14.78)
    j = Node(62)
    k = Node(500)
    m = Node(30000.19)
    n = Node(40000)

    a.le = b
    a.ri = c
    b.le = d
    b.ri = e
    c.le = f
    c.ri = g
    d.le = h
    d.ri = i
    e.le = j
    f.le = k
    f.ri = m
    m.ri = n

    return a


def do_task():
    disp = BinTreeDisplay()
    tree = create_tree()

    disp.config(
        struct_node=('key', 'le', 'ri'),
        space_branch_neighbor=2
    )

    res = disp.get(tree)
    print(res)
