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

  if len(in_order) == 0:
    return None
    
  current = post_order[-1]

  root = Node(current)

  mid = in_order.index(current)

  in_order_left = in_order[:mid]
  in_order_right = in_order[mid + 1 :]

  post_order_left = post_order[:len(in_order_left)]
  post_order_right = post_order[len(in_order_left): -1]

  root.left = build_tree_in_post(in_order_left, post_order_left)
  root.right = build_tree_in_post(in_order_right, post_order_right)

  return root



build_tree_in_post(
  [ 'd', 'b', 'e', 'a', 'f', 'c', 'g' ],
  [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 
)
#      a
#    /    \
#   b      c
#  / \    / \
# d   e  f   g