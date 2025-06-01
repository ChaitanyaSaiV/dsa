from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)

  distance = 0

  visited = set([node_A])

  queue = deque([(node_A, 0)])

  while queue:
    current, distance = queue.popleft()
    if current == node_B:
      return distance
    
    for node in graph[current]:
      if node not in visited:
        visited.add(node)
        queue.append((node, distance+1))
      

  return -1

def build_graph(edges):
  graph = {}

  for edge in edges:
    a, b = edge

    if a not in graph:
      graph[a] = []

    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)
  return graph



edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z'))