""" zipper lists
Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty. """


class Node:
 def __init__(self, val):
  self.val = val
  self.next = None

def zipper_lists(head_1, head_2):
  return_head = head_1

  tail = head_1

  c1 = head_1
  c2 = head_2

  i = 0

  while c1 is not None and c2 is not None:
    if i % 2 == 0:
      c1_next = c1.next
      tail.next = c2
      c1 = c1_next
    else:
      c2_next = c2.next
      tail.next = c1
      c2 = c2_next
      
    tail = tail.next
    i += 1

  if c1 is None:
    tail.next = c2
  else:
    tail.next = c1

  return return_head



a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)