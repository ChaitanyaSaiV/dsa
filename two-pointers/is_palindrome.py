""" is palindrome
Write a function, is_palindrome, that takes in a string and returns a boolean indicating whether or not the string is the same forwards and backwards. """


def is_palindrome(s):
  length = len(s)
  if length == 1 or length == 0:
    return True
    
  if s[0] == s[length - 1]:
    return is_palindrome(s[1:length-1])
  else:
    return False
  



is_palindrome("kayak") 