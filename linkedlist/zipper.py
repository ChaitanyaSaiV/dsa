""" zipper lists
Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty. """


class Node:
 def __init__(self, val):
  self.val = val
  self.next = None

def zipper_lists(head_1, head_2):
  original_head = head_1
  tail = head_1
  counter = 0
  current_1 = head_1.next
  current_2 = head_2
  while current_1 is not None and current_2 is not None:
    if counter % 2 == 0:
      tail.next = current_2
      current_2 = current_2.next
    else:
      tail.next = current_1
      current_1 = current_1.next
    tail = tail.next
    counter += 1

  if current_1 is not None:
    tail.next = current_1
  if current_2 is not None:
    tail.next = current_2
    
  return original_head



s = Node("s")
t = Node("t")
s.next = t
# s -> t

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.next = two
two.next = three
three.next = four
# 1 -> 2 -> 3 -> 4

zipper_lists(s, one)