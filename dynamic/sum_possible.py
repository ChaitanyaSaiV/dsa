def sum_possible(amount, numbers):
  if amount == 0:
    return True
  
  if amount < 0:
    return False
    
  for number in numbers:
    if sum_possible(amount - number, numbers) == True:
      return True
    
  return False


sum_possible(8, [5, 12, 4])
