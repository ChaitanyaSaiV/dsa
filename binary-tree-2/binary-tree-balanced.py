""" is tree balanced
Write a function, is_tree_balanced, that takes in the root of a binary tree. 

The function should return a boolean indicating whether or not the tree is "balanced".

A "balanced" binary tree is a binary tree where the height between the left and right subtrees differs by at most 1 for every node. """


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def check_height_balance(root):
    if root is None:
        return 0

    left_height = check_height_balance(root.left)
    if left_height == -1:
        return -1

    right_height = check_height_balance(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1
    else:
        return 1 + max(left_height, right_height)

def is_tree_balanced(root):
    return check_height_balance(root) > -1


a = Node("a")
b = Node("b")
c = Node("c")

a.left = b
a.right = c

#         a
#       /   \
#      b    c

is_tree_balanced(a) # -> True