""" Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

If the tree is empty, return -1. """



class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


from collections import deque

def how_high(node):
  height = -1

  if node is None:
    return height
  queue = deque([(node,0)])

  while queue:
    current, length = queue.popleft()
    height = max(height, length)
    if current.right is not None:
      queue.append((current.right, length+1))
    if current.left is not None:
      queue.append((current.left, length+1))


  return height



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

how_high(a) # -> 2