""" linked list cycle
Write a function, linked_list_cycle, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains a cycle. """


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_cycle(head):
  slow = head
  fast = head
  first_iteration = True
  while fast is not None and fast.next is not None:
    if slow == fast and not first_iteration:
      return True
    first_iteration = False
    slow = slow.next
    fast = fast.next.next

  return False



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d 

linked_list_cycle(a) 
