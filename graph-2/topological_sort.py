""" topological order

Write a function, topological_order, that takes in a dictionary representing the adjacency list for a directed-acyclic graph. 

The function should return a list containing the topological-order of the graph.

The topological ordering of a graph is a sequence where "parent nodes" appear before their "children" within the sequence. """


def topological_order(graph):
  num_parents = {}

  result = []

  for node in graph:
    num_parents[node] = 0
  
  for node in graph:
    for neighbor in graph[node]:
      num_parents[neighbor] += 1

  ready = []
  
  for key in num_parents:
    if num_parents[key] == 0:
      ready.append(key)

  while len(ready) > 0:
    current = ready.pop()
    result.append(current)
    for node in graph[current]:
      num_parents[node] -= 1
      if num_parents[node] == 0:
        ready.append(node)
        
  return result



topological_order({
  "a": ["f"],
  "b": ["d"],
  "c": ["a", "f"],
  "d": ["e"],
  "e": [],
  "f": ["b", "e"],
}) # -> ['c', 'a', 'f', 'b', 'd', 'e']