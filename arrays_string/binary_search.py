""" binary search
Write a function, binary_search, that takes in a sorted list of numbers and a target. The function should return the index where the target can be found within the list. If the target is not found in the list, then return -1.

You may assume that the input array contains unique numbers sorted in increasing order.

Your function must implement the binary search algorithm. """



def binary_search(numbers, target):
  low = 0
  high = len(numbers) - 1
  while low <= high:
    mid = (high + low) // 2
    if numbers[mid] > target:
      high = mid - 1
    elif numbers[mid] < target:
      low = mid + 1
    else:
      return mid

  return -1





binary_search([0, 6, 8, 12, 16, 19, 20, 28], 8) # -> 2
