class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def path_finder(root, target):
  if root is None:
    return None
    
  if root.val == target:
    return [root.val]

  left = path_finder(root.left, target)

  right = path_finder(root.right, target)
 

  if left is not None and len(left) > 0:
    return [root.val, *left]
  if right is not None and len(right) > 0:
    return [root.val, *right]
    
  return None




a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]