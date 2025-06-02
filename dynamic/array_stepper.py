def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})


def _array_stepper(numbers, i , memo):
  if i in memo:
    return memo[i]
  if len(numbers[i:]) == 1:
    return True
  if numbers[i] == 0:
    memo[i] == False
    return False

  for index in range(1, numbers[i] + 1):
    value = _array_stepper(numbers, i + index, memo)
    if value:
      return True

  memo[i] = False
  return memo[i]

  
print(array_stepper([2, 4, 2, 0, 0, 1]))