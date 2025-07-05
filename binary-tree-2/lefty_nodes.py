""" lefty nodes
Write a function, lefty_nodes, that takes in the root of a binary tree. 
The function should return a list containing the left-most value on every level of the tree. 
The list must be ordered in a top-down fashion where the root is the first item.

Note that the left-most node on a level may not necessarily be a left child. """

from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None   


def lefty_nodes(root):
  level = 0
  lefty_nodes = [root.val]
  queue = deque([(root, 0)])

  while queue:
    current, current_level = queue.popleft()
    if current_level != level:
      lefty_nodes.append(current.val)
      level = current_level

    if current.left is not None:
      queue.append((current.left, current_level + 1))
    if current.right is not None:
      queue.append((current.right, current_level + 1))
    
  return lefty_nodes






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

lefty_nodes(a) # [ 'a', 'b', 'd', 'g' ]