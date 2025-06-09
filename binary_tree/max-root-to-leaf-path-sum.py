class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def max_path_sum(root):
  if not root:
    return float("-inf")
  if root.left is None and root.right is None:
    return root.val
  return root.val + max(max_path_sum(root.right), max_path_sum(root.left))




a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(0)
f = Node(-13)
g = Node(-1)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   0    -13
#     /       \
#    -1       -2

max_path_sum(a) # -> -8