""" post order
Write a function, post_order, that takes in the root of a binary tree. The function should return a list containing the post-ordered values of the tree.

Post-order traversal is when nodes are recursively visited in the order: left child, right child, self. """


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def post_order(root):
  values = []
  return _post_order(root, values)

def _post_order(root, values):
  if root is None:
    return []
  
  _post_order(root.left, values)
  _post_order(root.right, values)
  values.append(root.val)

  return values


x = Node('x')
y = Node('y')
z = Node('z')

x.left = y
x.right = z

#       x
#    /    \
#   y      z

post_order(x)
# ['y', 'z', 'x']