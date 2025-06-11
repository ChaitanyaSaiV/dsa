""" largest component
Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph. """



def largest_component(graph):
  visited = set()
  island_count = 0
  for node in graph:
    current_size = explore_island(graph, node, visited)
    island_count = max(island_count, current_size)

  return island_count


def explore_island(graph, node, visited):
  if node in visited:
    return 0
  else:
    size = 1
    visited.add(node)
    for neighbor in graph[node]:
      size += explore_island(graph, neighbor, visited)
  return size


largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4