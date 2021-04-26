from sutree.display.valueutil import ValueUtil
from sutree.display.bintreeparser import BinTreeParser


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
    c.ri = d

    return a


def do_task():
    vutil = ValueUtil()
    parser = BinTreeParser(vutil)
    tree = create_tree()

    parser.config(struct_node=('key', 'le', 'ri'))

    parsing_tree = parser.build_tree(tree)
    parser.convert_margin_local_to_global(parsing_tree, 0)

    print(parsing_tree)
