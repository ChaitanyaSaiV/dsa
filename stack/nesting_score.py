""" nesting score
Write a function, nesting_score, that takes in a string of brackets as an argument. The function should return the score of the string according to the following rules:

[] is worth 1 point
XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are their respective scores
[S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring
You may assume that the input only contains well-formed square brackets. """


def nesting_score(string):
  stack = []

  for char in string:
    if char == '[':
      stack.append(char)
    else:
      segment = 0
      while stack[-1] != "[":
        popped = stack.pop()
        segment += popped
      stack.pop()
      if segment == 0:
        segment += 1
      else:
        segment *= 2
      stack.append(segment)

  score = 0
  while stack:
    score += stack.pop()
  return score



nesting_score("[[][]][]") # -> 5