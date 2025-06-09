""" is subsequence
Write a function, is_subsequence, that takes in string_1 and string_2. The function should return a boolean indicating whether or not string_1 is a subsequence of string_2.

A subsequence is a string that can be formed by deleting 0 or more characters from another string. """


def is_subsequence(string_1, string_2):
  i = 0
  j = 0
  while i < len(string_1) and j < len(string_2):
    if string_1[i] == string_2[j]:
      i += 1
      j += 1
    else:
      j += 1 
  return i == len(string_1)



is_subsequence("bde", "abcdef") 