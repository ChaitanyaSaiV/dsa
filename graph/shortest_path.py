""" shortest path
Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1. You can assume that A and B exist as nodes in the graph. """

from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = generate_graph(edges)
  weight = 0
  visited = set(node_A)
  queue = deque([(node_A, 0)])

  while queue:
    current, length = queue.popleft()
    if current == node_B:
      return length
    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, length + 1))

  return -1


def generate_graph(edges):
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

shortest_path(edges, 'w', 'z') 