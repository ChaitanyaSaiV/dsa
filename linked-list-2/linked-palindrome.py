""" linked palindrome
Write a function, linked_palindrome, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list is a palindrome. A palindrome is a sequence that is the same both forwards and backwards. """

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_palindrome(head):
  stack = []

  slow = head
  fast = head

  while fast is not None:
    if fast.next is None:
      slow = slow.next
      fast = None
      continue
    stack.append(slow.val)
    slow = slow.next
    fast = fast.next.next

  while slow is not None:
    current = stack.pop()
    if current != slow.val:
      return False
    else:
      slow = slow.next
  
  return True




a = Node(0)
b = Node(1)
c = Node(0)
d = Node(1)
e = Node(0)

a.next = b
b.next = c
c.next = d
d.next = e

# 3 -> 2 -> 7 -> 7 -> 2 -> 3
linked_palindrome(a) 