""" is palindrome
Write a function, is_palindrome, that takes in a string and returns a boolean indicating whether or not the string is the same forwards and backwards. """


def is_palindrome(s):
  if not s:
    return True

  if s[0] != s[-1]:
    return False

  return is_palindrome(s[1:-1])
  



is_palindrome("pops") 