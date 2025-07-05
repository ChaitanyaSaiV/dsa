""" is binary search tree
Write a function, is_binary_search_tree, that takes in the root of a binary tree. 

The function should return a boolean indicating whether or not the tree satisfies the binary search tree property.

A Binary Search Tree is a binary tree where all values within a node's left subtree are smaller than the node's value and all values in a node's right subtree are greater than the node's value. """



class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def is_binary_search_tree(root):
  stack = []
  stack = _is_binary_search_tree(root, stack)
  prev = float("-inf")

  for val in stack:
    if val < prev:
      return False
    prev = val
  return True


def _is_binary_search_tree(root, stack):
  if root is None:
    return []
  
  _is_binary_search_tree(root.left, stack)

  stack.append(root.val)

  _is_binary_search_tree(root.right, stack)

  return stack




a = Node(12)
b = Node(5)
c = Node(18)
d = Node(3)
e = Node(15)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     18
#  / \     \
# 3   15     19

is_binary_search_tree(a) # -> False
