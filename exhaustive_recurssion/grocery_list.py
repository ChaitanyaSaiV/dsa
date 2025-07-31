""" grocery budget
Write a function, grocery_budget, that takes in grocery_list and a number budget. Every item in grocery_list is a pair containing the item name and price. Your function should return all possible ways to purchase items without spending more than the given budget.

The order of the items in the return value does not matter.

You cannot purchase an item more than once. You do not have to spend the budget fully. """

def grocery_budget(grocery_list, budget):
  grocery_graph = build_graph(grocery_list)

  print(grocery_graph)


def build_permutations(grocery_graph, budget):
  if budget == 0:
    return []
  
  

def build_graph(grocery_list):
  graph = {}

  for grocery in grocery_list:
    item, price = grocery

    graph[item] = price
  
  return graph

grocery_budget([  
  ('eggs', 5),
  ('milk', 3),
  ('butter', 3)
], 7) # ->
# [ 
#   [ 'eggs' ], 
#   [ 'butter', 'milk' ], 
#   [ 'milk' ], 
#   [ 'butter' ], 
#   [] 
# ] 