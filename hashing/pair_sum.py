def pair_sum(numbers, target_sum):
  dict = {}
  counter = 0
  for number in numbers:
    if number in dict:
      return (dict[number], counter)
    else:
      remainder = target_sum - number
      dict[remainder] = counter
      counter += 1
  return (0, 1)




print(pair_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)