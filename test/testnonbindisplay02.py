from pytreedisplay import NonBinTreeDisplay


class Node:
    def __init__(self, key):
        self.key = key
        self.children = []


def create_tree():
    a = Node('func_definition')
    b = Node('def')
    c = Node('func_name')
    d = Node('(')
    e = Node('arg_list')
    f = Node(')')
    g = Node('sum_2_integers')
    h = Node('arg')
    i = Node(',')
    j = Node('arg')
    k = Node('foo')
    m = Node('bar')

    a.children.append(b)
    a.children.append(c)
    a.children.append(d)
    a.children.append(e)
    a.children.append(f)

    c.children.append(g)

    e.children.append(h)
    e.children.append(i)
    e.children.append(j)

    h.children.append(k)
    j.children.append(m)

    return a


def do_task():
    tree = create_tree()
    disp = NonBinTreeDisplay()

    disp.config(
        leaf_at_bottom=True,
        space_branch_neighbor=3
    )

    res = disp.get(tree)
    print(res)
