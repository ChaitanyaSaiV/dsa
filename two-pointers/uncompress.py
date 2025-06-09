""" uncompress
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern: """



def uncompress(s):
  numbers = '0123456789'
  i = 0
  j = 0
  result = []
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      length = int(s[i:j])
      result.append(s[j] * length)
      j += 1
      i = j

  return "".join(result)



uncompress("2c3a1t") # -> 'ccaaat'