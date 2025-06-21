""" min change
Write a function min_change that takes in an amount and a list of coins. The function should return the minimum number of coins required to create the amount. You may use each coin as many times as necessary.

If it is not possible to create the amount, then return -1. """

def min_change(amount, coins):

  return _min_change(amount, coins, {})

def _min_change(amount, coins, memo):
  if amount == 0:
    return 0
  if amount < 0:
    return float("inf")
  
  if amount in memo:
    return memo[amount]
  
  min_coins = float("inf")
  
  for coin in coins:
    current_min_coins = _min_change(amount - coin, coins, memo)
    if current_min_coins < min_coins:
      min_coins = current_min_coins

  if min_coins == float("inf"):
    memo[amount] = -1
  else:
    memo[amount] = min_coins + 1

  return memo[amount]
      

print(min_change(23, [2, 5, 7]))