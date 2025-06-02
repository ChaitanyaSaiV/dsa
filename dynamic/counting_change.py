def counting_change(amount, coins):
  if amount < 0:
    return -1
  
  if amount == 0:
    return 0

  count = 1
  for coin in coins:
    returnCount = counting_change(amount - coin, coins)
    if returnCount > 0:
      count += returnCount

  return count


print(counting_change(5, [1, 2, 3]))