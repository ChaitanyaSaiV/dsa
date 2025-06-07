class Node:
 def __init__(self, val):
  self.val = val
  self.next = None

def reverse_list(head):
  current = head
  prev = None
  while current is not None:
    dummy = current
    current.next = prev
    prev = dummy
    current = dummy.next
  return current



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

reverse_list(a)