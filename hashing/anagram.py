""" anagrams
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. 
Anagrams are strings that contain the same characters, but in any order. """


""" def anagrams(s1, s2):
  ana_s1 = {}
  ana_s2 = {}
  for char in s1:
    if char in ana_s1:
      ana_s1[char] += 1
    else:
      ana_s1[char] = 1
  for char in s2:
    if char in ana_s1:
      ana_s2[char] += 1
    else:
      ana_s2[char] = 1
  return ana_s2 == ana_s1 """


def dict(string):
  returnVal = {}
  for char in string:
    if char in returnVal:
      returnVal[char] += 1
    else:
      returnVal[char] = 1
  return returnVal

print(anagrams('restful', 'fluster') )