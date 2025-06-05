""" all unique
Write a function, all_unique, that takes in a list. The function should return a boolean indicating whether or not the list contains unique items. """


def all_unique(items):
  uItems = set(items)
  return len(items) == len(uItems)



all_unique(["q", "r", "s", "a"]) # -> True