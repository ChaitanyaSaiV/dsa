""" undupe sorted linked list
Write a function that takes in a linked list that contains values in increasing order. The function should return a new linked list containing the original values, with duplicates removed. The relative order of values in the resulting linked list should be unchanged. """



class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def undupe_sorted_linked_list(head):
  tail = head
  current = head
  prev = Node(None)
  while current is not None:
    if prev.val == current.val:
      prev.next = current.next
      current = current.next
    else:
      prev = current
      current = current.next
  
  return tail



a = Node(4)
b = Node(4)
c = Node(6)
d = Node(6)
e = Node(6)
f = Node(7)
g = Node(7)

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
f.next = g;

# 4 -> 4 -> 6 -> 6 -> 6 -> 7 -> 7

undupe_sorted_linked_list(a) # 4 -> 6 -> 7
