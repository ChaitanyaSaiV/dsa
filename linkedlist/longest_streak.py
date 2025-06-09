""" longest streak
Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.

 """

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def longest_streak(head):
  current = head.val
  maxStreak = float("-inf")
  currentStreak = 0
  while head is not None:
    if head.val == current:
      currentStreak += 1
    else:
      current = head.val
      if maxStreak < currentStreak:
        maxStreak = currentStreak
        currentStreak = 1
    head = head.next

  if maxStreak < currentStreak:
    maxStreak = currentStreak

  return maxStreak

a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9

longest_streak(a)