def longest_path(graph):
  distance = {}

  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0

  for node in graph:
    explore(graph, node, distance)

  return max(distance.values())


def explore(graph, node, distance):
  if node in distance:
    return distance[node]
  max_distance = 0
  for neighbor in graph[node]:
    attempt = explore(graph, neighbor, distance)
    if attempt > max_distance:
      max_distance = attempt
  distance[node] = max_distance + 1
  return distance[node]

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

longest_path(graph) 