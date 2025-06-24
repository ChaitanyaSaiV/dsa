def paired_parentheses(string):
  stack = []

  for char in string:
    if char == "(":
      stack.append(char)
    if char == ")":
      if len(stack) == 0:
        return False
      if stack.pop() != "(":
        return False

  return len(stack) == 0


paired_parentheses("()rose(jeff")