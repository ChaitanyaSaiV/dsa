class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def depth_first_values(root):
  if not root:
    return []
  result = []
  stack = [ root ]
  while stack:
    current = stack.pop()
    result.append(current.val)

    if current.right is not None:
      stack.append(current.right)

    
    if current.left is not None:
      stack.append(current.left)

      
  return result



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

depth_first_values(a)