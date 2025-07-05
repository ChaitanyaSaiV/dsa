""" add lists
Write a function, add_lists, that takes in the head of two linked lists, each representing a number. 

The nodes of the linked lists contain digits as values. 

The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. 

The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

You must do this by traversing through the linked lists once. 

Say we wanted to compute 621 + 354 normally. The sum is 975:

   621
 + 354
 -----
   975

Then, the reversed linked list format of this problem would appear as:

    1 -> 2 -> 6
 +  4 -> 5 -> 3
 --------------
    5 -> 7 -> 9
"""


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  dummy = Node(None)
  tail = dummy

  while head_1 is not None or head_2 is not None:
    current_val = getattr(head_1, "val", 0) + getattr(head_2, "val", 0)
    tail.next = Node(current_val)
    tail = tail.next
    if head_1 is not None:
      head_1 = head_1.next
    if head_2 is not None:
      head_2 = head_2.next

  return dummy.next




#   621
# + 354
# -----
#   975

a1 = Node(1)
a2 = Node(2)
a3 = Node(6)
a1.next = a2
a2.next = a3
# 1 -> 2 -> 6

b1 = Node(4)
b2 = Node(5)
b3 = Node(3)
b1.next = b2
b2.next = b3
# 4 -> 5 -> 3

add_lists(a1, b1)