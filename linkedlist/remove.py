class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def remove_node(head, target_val):
  current = head
  prev = head
  while current is not None:
    if current.val == target_val:
      prev.next = current.next
      return head
    else:
      prev = current
      current = current.next
      
  return head



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

remove_node(a, "c")