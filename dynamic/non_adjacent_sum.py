def _non_adjacent_sum(nums):
  if len(nums) == 0:
    return 0

  include = nums[0] + _non_adjacent_sum(nums[i+2:])
  exclude =  _non_adjacent_sum(nums[i+1:])

  return max(include, exclude)