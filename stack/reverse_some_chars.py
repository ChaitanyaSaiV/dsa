""" reverse some chars
Write a function, reverse_some_chars, that takes in string and an list of characters. The function should return the string with the order of the given characters in reverse. """



def reverse_some_chars(s, chars):
  stack = []
  chars = set(chars)
  for char in s:
    if char in chars:
      stack.append(char)

  response = []

  for char in s:
    if char in chars:
      response.append(stack.pop())
    else:
      response.append(char)

  return "".join(response)




reverse_some_chars("computer", ["a", "e", "i", "o", "u"]) # -> 'cemputor'