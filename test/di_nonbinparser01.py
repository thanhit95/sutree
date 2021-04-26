from sutree.display.valueutil import ValueUtil
from sutree.display.nonbintreeparser import NonBinTreeParser


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
    vutil = ValueUtil()
    parser = NonBinTreeParser(vutil)
    tree = create_tree()

    parsing_tree = parser.build_tree(tree)
    parser.convert_margin_local_to_global(parsing_tree, 0)

    print(parsing_tree)
