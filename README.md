# SUTREE

## DESCRIPTION

Tree data structure library with great display utility.

&nbsp;

## AUTHOR

Thanh Trung Nguyen

- Email: thanh.it1995@gmail.com
- Facebook: <https://www.facebook.com/thanh.it95>

&nbsp;

## INSTALLATION

```shell
pip install sutree
```

&nbsp;

## FEATURES

This package includes two libraries:

- Tree library.
- Tree display library.

TODO feature: Implement B-Tree.

**Tree library:**

- Two types of trees: Binary Search Tree, AVL Tree.
- Regular operations:
  - Checking empty.
  - Getting number of nodes.
  - Getting height.
  - Traversal:
    - 3 options: pre-order, in-order, post-order.
    - 2 modes: recursive traversal and non-recursive traversal.
  - Checking existence of a key.
  - Getting minimum key.
  - Getting maximum key.
  - Insertion.
  - Removal.
  - Constructing from a list.

**Tree display library:**

- It can config space between 2 branch neighbors.
- It can config precision of floating-point numbers.
- It accepts any type of key of node. Just makes sure key is convertible to string.
- It accepts any structure of node, which is high flexibily.
- It can config left margin.
- It outputs to:
  - a string, or...
  - a list of rows.

Output example generated by this utility:

Output example 1:

```text
                       100
                        |
             -----------------------
             50                  70000
             |                     |
       -------------        ----------------
       10        88.52    20000          90000
       |           |        |
   ---------    ----     --------
-123456  14.78  62      500  30000.19
                                |
                                -----
                                  40000
```

Output example 2:

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

&nbsp;

## TUTORIALS

There are two sections of tutorials:

- Tree: Using pre-defined trees in library such as BinaryTree, AvlTree...
  - Take a look at ```/test/tree_```.
- Display: Display a tree.
  - Read [tutorials_display.md](tutorials_display.md)

&nbsp;

## CODE STRUCTURE

Update later.

&nbsp;

## PROJECT SPECIFICATIONS

- Language: Python 3.8
- Paradigms: object-oriented, procedural

&nbsp;

## LICENSE

Copyright (c) Thanh Trung Nguyen.

This project is licensed under the [3-Clause BSD License](LICENSE.txt).
