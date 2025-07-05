""" middle value
Write a function, middle_value, that takes in the head of a linked list as an argument. The function should return the value of the middle node in the linked list. If the linked list has an even number of nodes, then return the value of the second middle node.

You may assume that the input list is non-empty. """


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def middle_value(head):
  slow = head
  fast = head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  return slow
    

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.next = b
b.next = c
c.next = d
d.next = e

# a -> b -> c -> d -> e
middle_value(a) # c