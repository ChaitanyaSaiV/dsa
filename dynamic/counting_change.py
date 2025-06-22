""" counting change
Write a function, counting_change, that takes in an amount and a list of coins. The function should return the number of different ways it is possible to make change for the given amount using the coins.

You may reuse a coin as many times as necessary.


For example,

counting_change(4, [1,2,3]) -> 4

There are four different ways to make an amount of 4:

1. 1 + 1 + 1 + 1
2. 1 + 1 + 2
3. 1 + 3
4. 2 + 2
 """


def counting_change(amount, coins):
  memo = {}
  return _counting_change(amount, coins, 0, {})


def _counting_change(amount, coins, i, memo):
  key = (amount, i)
  if key in memo:
    return memo[key]
  if amount == 0:
    return 1
  
  if i >= len(coins):
    return 0
  
  coin = coins[i]

  total = 0

  for qty in range (0, (amount // coin ) + 1):
    remainder = amount - (coin * qty)
    total += _counting_change(remainder, coins, i + 1, memo)

  memo[key] = total

  return total


""" def _counting_change(amount, coins, memo):

  if amount in memo:
    return memo[amount]


  if amount == 0:
    return 1
  
  if amount < 0:
    return 0
  
  count = 0
  
  for coin in coins:
    current_count = _counting_change(amount - coin, coins, memo)
    if current_count > 0:
      count += current_count

  memo[amount] = count

  return memo[amount] """








counting_change(4, [1, 2, 3]) # -> 4