""" undirected path
Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B. """



from collections import deque





def undirected_path(edges, node_A, node_B):
  visited = set()

  graph = build_graph(edges)

  queue = deque([node_A])

  while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
      if current == node_B:
        return True
      if neighbor not in visited:
        queue.append(neighbor)
        visited.add(neighbor)
        
  return False



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
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'j', 'm') 