""" sum possible
Write a function sum_possible that takes in an amount and a list of positive numbers. The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative. """


def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})


def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]
    
  if amount < 0:
    return False
    
  if amount == 0:
    return True
    
  for number in numbers:
    remainder = amount - number
    if _sum_possible(remainder, numbers, memo):
      memo[amount] = True
      return True
    
  memo[amount] = False
  
  return False


sum_possible(8, [5, 12, 4]) # -> True, 4 + 4