""" overlap subsequence
Write a function, overlap_subsequence, that takes in two strings as arguments. The function should return the length of the longest overlapping subsequence.

A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters. """


def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0, {})


def _overlap_subsequence(string_1, string_2, i, j, memo):
  key = (i, j)

  if key in memo:
    return memo[key]
  
  if i > len(string_1) - 1 or j > len(string_2) - 1:
    return 0
  
  if string_1[i] == string_2[j]:
    memo[key] = 1 + _overlap_subsequence(string_1, string_2, i + 1, j + 1, memo)
  
  else:
    memo[key] = max(_overlap_subsequence(string_1, string_2, i + 1, j, memo), _overlap_subsequence(string_1, string_2, i , j + 1, memo))
  

  return memo[key]



overlap_subsequence("dogs", "daogt") # -> 3