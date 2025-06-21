""" non adjacent sum
Write a function, non_adjacent_sum, that takes in a list of numbers as an argument. The function should return the maximum sum of non-adjacent items in the list. There is no limit on how many items can be taken into the sum as long as they are not adjacent. """


def non_adjacent_sum(nums):
  max_value = float("-inf")

  for i in range(len(nums)):

    current = _non_adjacent_sum(nums, i, {})
    max_value = max(max_value, current)

  return max_value

def _non_adjacent_sum(nums, i, memo):
  if i >= len(nums):
    return 0
  
  if i == len(nums) - 1:
    return nums[i]
  
  if i in memo:
    return memo[i]
  
  include = _non_adjacent_sum(nums, i + 2, memo)
  exclude = _non_adjacent_sum(nums, i + 3, memo)
  memo[i] = nums[i] + max(include, exclude)
  return memo[i]


nums = [2, 4, 5, 12, 7]
print(non_adjacent_sum(nums)) # -> 16