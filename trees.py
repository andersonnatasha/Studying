# Breath first search

#                             1
#             2                                3
#     4           5                       6           7
# 9                   10              11      12


class Node():
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

        # if children is None:
        # self.children = children or []

    def __repr__(self):
        return f'<Node = {self.data}>'


class Tree():
    """A Tree"""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return f'<Tree = {self.root}>'


hogwarts = Tree(Node("Dumbeldore", []))


def breadth_first_search(root, target):

    to_visit = []
    #Snape, Ron
    # Harry
    if root.data == target:
        return True

    to_visit.append(root.children)

    while to_visit:
        checking = to_visit.pop(0)
        if checking.data == target:
            return True
        to_visit.extend(checking.children)


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
