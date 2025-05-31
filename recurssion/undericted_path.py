def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)

  visited = set()

  return explore(graph, node_A, node_B, visited)


def explore(graph, src, dst, visited):
  if src == dst: return True

  if src in visited:
    return False
  
  visited.add(src)
  
  for node in graph[src]:
    if explore (graph, node, dst, visited) == True: return True
  
  return False


def build_graph(edges):
  graph = {}
  for edge in edges:
    a,b = edge
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

print(undirected_path(edges, 'k', 'o') )