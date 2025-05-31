def connected_components_count(graph):
  visited = set()
  count = 0

  for node in graph:
    if explore(graph, node, visited) == True:
      count += 1

  return count

def explore(graph, src, visited):
  if src in visited:
    return False

  visited.add(src)

  for node in graph[src]:
    explore(graph, node, visited)
  
  return True
  

connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) 