""" build tree in post
Write a function, build_tree_in_post, that takes in a list of in-ordered values and a list of post-ordered values for a binary tree. 

The function should build a binary tree that has the given in-order and post-order traversal structure. The function should return the root of this tree.

You can assume that the values of inorder and postorder are unique. """


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_post(in_order, post_order):
  pass # todo



build_tree_in_post(
  [ 'y', 'x', 'z' ],
  [ 'y', 'z', 'x' ] 
)
#       x
#    /    \
#   y      z