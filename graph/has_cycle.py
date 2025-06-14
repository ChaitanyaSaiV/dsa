""" has cycle
Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph. The function should return a boolean indicating whether or not the graph contains a cycle. """


def has_cycle(graph):
  for node in graph:
    if explore(graph, node, set()):
      return True
  return False


def explore(graph, node, visited):
  if len(graph[node]) == 0:
    return False
    
  if node in visited:
    return True

  visited.add(node)

  for neighbor in graph[node]:
    if explore(graph, neighbor, visited):
      return True

  return False

has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
}) # -> False