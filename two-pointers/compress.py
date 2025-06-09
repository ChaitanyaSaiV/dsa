""" compress
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed. """


def compress(s):
  s += '!'
  i = 0
  j = 0
  result = []
  while j < len(s):
    if s[i] == s[j]:
      j += 1
    else:
      length = j - i
      if length == 1:
        result.append(s[i])
      else:
        result.append(str(length))
        result.append(s[i])
      i = j
  return "".join(result)



compress('ccaaatsss') # -> '2c3at3s'