""" exclusive items
Write a function, exclusive_items, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in either list but not both lists.

You may assume that each input list does not contain duplicate elements. """


def exclusive_items(a, b):
  a_set = set(a)
  b_set = set(b)
  result = []
  for item in a:
    if item not in b_set:
      result.append(item)
  for item in b:
    if item not in a_set:
      result.append(item)

  return result


exclusive_items([4,2,1,6], [3,6,9,2,10]) # -> [4,1,3,9,10]