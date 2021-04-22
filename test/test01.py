from display import BinTreeDisplay


class Node:
    def __init__(self, value):
        self.myvalue = value
        self.le = None
        self.ri = None


#########################################


def do_task():
    a = Node(123)
    b = Node(45)
    c = Node('hello')
    d = Node(6)

    a.le = b
    a.ri = c
    b.ri = d

    disp = BinTreeDisplay()

    disp.config(struct_node=('myvalue', 'le', 'ri'))

    print(disp.get(a))
