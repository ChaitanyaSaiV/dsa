""" binary search tree includes
Write a function, binary_search_tree_includes, that takes in the root of a binary search tree containing numbers and a target value. 

The function should return a boolean indicating whether or not the target is found within the tree.

A Binary Search Tree is a binary tree where all values within a node's left subtree are smaller than the node's value and all values in a node's right subtree are greater than or equal to the node's value.

Your solution should have a best case runtime of O(log(n)). """


""" Recursive Solution:


def binary_search_tree_includes(root, target):
  if root is None:
    return False

  if root.val == target:
    return True

  if root.val > target:
    return binary_search_tree_includes(root.left, target)
  else:
    return binary_search_tree_includes(root.right, target) """


from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def binary_search_tree_includes(root, target):
  queue = deque([root])

  while queue:
    length = len(queue)
    for i in range(length):
      current = queue.popleft()

      if current.val == target:
        return True

      if current.val > target:
        if current.left is not None:
          queue.append(current.left)
        else:
          return False
      else:
        if current.right is not None:

         queue.append(current.right)
        else:
          return False
        
  return False
        




a = Node(12)
b = Node(5)
c = Node(18)
d = Node(3)
e = Node(9)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     18
#  / \     \
# 3   9     19


print(binary_search_tree_includes(a, 9)) # -> True