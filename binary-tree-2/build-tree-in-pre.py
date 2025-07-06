""" build tree in pre
Write a function, build_tree_in_pre, that takes in a list of in-ordered values and a list of pre-ordered values for a binary tree. 

The function should build a binary tree that has the given in-order and pre-order traversal structure. The function should return the root of this tree.

You can assume that the values of inorder and preorder are unique. """


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_pre(in_order, pre_order):
  if len(pre_order) == 0:
    return None

  val = pre_order[0]
  root = Node(val)
  idx = in_order.index(val)

  left_in_order = in_order[:idx]
  right_in_order = in_order[idx + 1:]

  left_pre_order = pre_order[1: 1 + len(left_in_order)]
  right_pre_order = pre_order[1 + len(left_in_order):]

  root.left = build_tree_in_pre(left_in_order, left_pre_order)
  root.right = build_tree_in_pre(right_in_order, right_pre_order)

  return root



build_tree_in_pre(
  [ 'z', 'y', 'x' ],
  [ 'y', 'z', 'x' ] 
)
#       y
#    /    \
#   z      x