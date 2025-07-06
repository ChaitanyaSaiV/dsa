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
  if len(post_order) == 0:
    return None
  
  val = post_order[-1]
  root = Node(val)
  root_idx = in_order.index(val)

  left_in_order = in_order[:root_idx]
  right_in_order = in_order[root_idx + 1:]

  left_post_order = post_order[:len(left_in_order)]
  right_post_order = post_order[len(left_in_order):len(post_order)-1]

  root.left = build_tree_in_post(left_in_order, left_post_order)
  root.right = build_tree_in_post(right_in_order, right_post_order)

  return root



build_tree_in_post(
  [ 'y', 'x', 'z' ],
  [ 'y', 'z', 'x' ] 
)
#       x
#    /    \
#   y      z