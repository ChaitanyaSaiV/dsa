""" befitting brackets
Write a function, befitting_brackets, that takes in a string as an argument. The function should return a boolean indicating whether or not the string contains correctly matched brackets.

You may assume the string contains only characters: ( ) [ ] { } """

def befitting_brackets(string):
  braces = {
    ")" : "(",
    "}" : "{",
    "]" : "["
  }

  openingBraces = ("(", "[" , "{")

  stack = []

  for char in string:
    if char in openingBraces:
      stack.append(char)
    else:
      if len(stack) == 0 or braces[char] != stack.pop():
        return False

  return len(stack) == 0



befitting_brackets('(){}[](())') # -> True