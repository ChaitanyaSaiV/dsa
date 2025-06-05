""" intersection with dupes
Write a function, intersection_with_dupes, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are common to both input lists. The elements in the result should appear as many times as they occur in both input lists.

You can return the result in any order. """

def intersection_with_dupes(a, b):
  a_dict = {}
  b_dict = {}

  result = []

  for item in a:
    if item in a_dict:
      a_dict[item] += 1
    else:
      a_dict[item] = 1
  for item in b:
    if item in b_dict:
      b_dict[item] += 1
    else:
      b_dict[item] = 1

  for item in b:
    if item in a_dict:
      if a_dict[item] > 0:
        result.append(item)
        a_dict[item] -= 1
  return result


intersection_with_dupes(
  ["a", "b", "c", "b"], 
  ["x", "y", "b", "b"]
) # -> ["b", "b"]