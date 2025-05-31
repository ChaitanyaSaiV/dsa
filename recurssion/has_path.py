def has_path(graph, src, dst):
  visited = set()
  return explore(graph, src, dst, visited)


def explore(graph, src, dst, visited):
  if src == dst:
    return True
  
  if src in visited:
    return False
  
  visited.add(src)
  
  for neighbor in graph[src]:
    if explore(graph, neighbor, dst, visited) == True:
      return True

  return False



graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'a'))