""" most frequent char
Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty. """


def most_frequent_char(s):
  charCount = {}

  for char in s:
    if char in charCount:
      charCount[char] += 1
    else:
      charCount[char] = 1

  max = float("-inf")
  maxChar = ''

  for count in charCount:
    if charCount[count] > max:
      max = charCount[count]
      maxChar = count
  return max



most_frequent_char('bookeeper')