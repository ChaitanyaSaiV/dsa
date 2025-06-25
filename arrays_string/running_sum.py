""" running sum
Write a function, running_sum, that takes in a list of numbers. The function should return a new list of the same length where each element contains the running sum up to that index of the original list. """


""" For example, the i-th result should be the sum of all elements 0 to i:

result[i] = numbers[0] + numbers[1] + numbers[2] + ... + numbers[i] """

def running_sum(numbers):
  response = []
  prev = 0
  for num in numbers:
    sum = num + prev
    response.append(sum)
    prev = sum
  return response

running_sum([4, 2, 1, 6, 3, 6]) # -> [ 4, 6, 7, 13, 16, 22 ] 