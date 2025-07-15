""" union-find code II
Let's learn more about union-find algorithm by implementing size and path-compression. Watch the approach and walkthrough videos first.

Write a function, countComponents, that takes in a number of nodes (n) and a list of edges for an undirected graph. 

In the graph, nodes are labeled from 0 to n - 1. The function should return the number of connected components in the given graph.

Solve this by implementing the complete Union-Find algorithm with size and path-compression. """

def find(roots, node):
  if roots[node] == node:
    return node
  found = find(roots, roots[node])
  return found

def union(roots, sizes, node_a, node_b):
  root_node_a = find(roots, node_a)
  root_node_b = find(roots, node_b)
  if root_node_a == root_node_b:
    return
  if sizes[root_node_a] >= sizes[root_node_b]:
    roots[root_node_b] = root_node_a
    sizes[root_node_a] += sizes[root_node_b]
  else:
    roots[root_node_a] = root_node_b
    sizes[root_node_b] += sizes[root_node_a]

  return
  
def count_components(n, edges):
  roots = []
  sizes = []
  for i in range(n):
    roots.append(i)
  for i in range(n):
    sizes.append(1)
    
  for edge in edges:
    node_a, node_b = edge
    union(roots, sizes, node_a, node_b)
    
  count = 0
  for i in range(n):
    if i == roots[i]:
      count += 1
  return count

count_components(10, [
  (3, 2),
  (5, 4),
  (4, 3),
  (2, 1),
  (0, 1),
  (8, 9),
  (5, 6),
  (7, 8)
]) # -> 2