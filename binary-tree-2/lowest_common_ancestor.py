""" lowest common ancestor
Write a function, lowest_common_ancestor, that takes in the root of a binary tree and two values. 

The function should return the value of the lowest common ancestor of the two values in the tree.

You may assume that the tree values are unique and the tree is non-empty.

Note that a node may be considered an ancestor of itself. """



class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def lowest_common_ancestor(root, val1, val2):
  if root is None:
    return None

  left = lowest_common_ancestor(root.left, val1, val2)
  right = lowest_common_ancestor(root.right, val1, val2)

  current = None

  if root.val == val1:
    current = root.val

  if root.val == val2:
    current = root.val

  if left is not None and right is not None:
    return root.val

  if left is not None or right is not None:
    if current is not None:
      current = root.val
    elif left is not None:
      current = left
    else:
      current = right

  return current



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h



print(lowest_common_ancestor(a, 'g', 'c')) # a