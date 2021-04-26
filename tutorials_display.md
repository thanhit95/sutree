# SUTREE TUTORIALS - DISPLAY A TREE

## TUTORIALS

### TUTORIAL 1. Display a binary tree using BinSearchTree

```sutree``` library support ```BinSearchTree```, which make it easier to build a binary search tree.
Of course, you can combine ```BinTreeDisplay``` with ```BinarySearchTree```.

```python 3
from sutree import BinTreeDisplay, BinSearchTree

bst = BinSearchTree()
bst.insert(100)
bst.insert(50)
bst.insert(70000.123)
bst.insert(82)

disp = BinTreeDisplay()
print(bst.display(disp))
```

Result:

```text
    100
     |
------------
50      70000.12
|
----
   82
```

### TUTORIAL 2. Display a binary tree using customized node

```python 3
from sutree import BinTreeDisplay


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


a = Node(123)
b = Node(45)
c = Node('hello')
d = Node(6)

a.left = b
a.right = c
b.right = d

disp = BinTreeDisplay()

disp.config(struct_node=('value', 'left', 'right'))

print(disp.get(a))
```

Result:

```text
   123
    |
----------
45     hello
|
----
   6
```

### TUTORIAL 3. Configuring space between 2 branch neighbors

The more space, the more width of the tree.

```python 3
disp.config(space_branch_neighbor=5)
```

Result:

```text
     123
      |
--------------
45         hello
|
------
     6
```

### TUTORIAL 4. Configuring float precision

```python 3
from sutree import BinTreeDisplay


class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


a = Node(1.45678)
b = Node(-29.01)
c = Node('hello')

a.left = b
a.right = c

disp = BinTreeDisplay()

disp.config(
    struct_node=('value', 'left', 'right'),
    float_pre=3
)

print(disp.get(a))
```

Result:

```text
    1.457
      |
  ----------
-29.01   hello
```

### TUTORIAL 5. Display a non-binary tree

```python 3
from sutree import NonBinTreeDisplay


class Node:
    def __init__(self, key):
        self.key = key
        self.children = []


def create_tree():
    a = Node('Sentence')
    b = Node('She')
    c = Node('wrote')
    d = Node('a book')

    a.children.append(b)
    a.children.append(c)
    a.children.append(d)

    return a


tree = create_tree()
disp = NonBinTreeDisplay()

disp.config(
    struct_node=('key', 'children')
)

print(disp.get(tree))
```

Result:

```text
     Sentence
        |
 ----------------
 |      |       |
She   wrote   a book
```

### TUTORIAL 6. Display a complex non-binary tree

```python 3
from sutree import NonBinTreeDisplay


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


tree = create_tree()
disp = NonBinTreeDisplay()

disp.config(
    struct_node=('key', 'children')
)

print(disp.get(tree))
```

Result:

```text
               func_definition
                      |
 -------------------------------------------
 |          |          |         |         |
def     func_name      (      arg_list     )
            |                    |
      sum_2_integers        -----------
                            |    |    |
                           arg   ,   arg
                            |         |
                           foo       bar
```

### TUTORIAL 7. More settings

```python 3
disp.config(
    leaf_at_bottom=True,
    compact_vert_line=True,
    margin_left=10
)
```

Result:

```text
                         func_definition
                                |
           -------------------------------------------
           |      func_name      |      arg_list     |
           |          |          |         |         |
           |          |          |    -----------    |
           |          |          |   arg   |   arg   |
           |          |          |    |    |    |    |
           |          |          |    |    |    |    |
          def   sum_2_integers   (   foo   ,   bar   )
```
