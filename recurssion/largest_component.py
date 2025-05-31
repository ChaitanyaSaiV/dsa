def largest_component(graph):
  visited = set()
  maxComponent = 0

  for node in graph:
    count = explore(graph, node, visited)
    if count > maxComponent:
      maxComponent = count
  return maxComponent

def explore(graph, node, visited):
  if node in visited:
    return 0
  
  count = 1

  visited.add(node)

  for neighbor in graph[node]:
    count += explore(graph, neighbor, visited)

  return count


print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}))