""" union-find code I
Write a function, count_components, that takes in a number of nodes (n) and a list of edges for an undirected graph. 

In the graph, nodes are labeled from 0 to n - 1. The function should return the number of connected components in the given graph.

This will be practice for implementing the basic Union-Find algorithm for graphs.

Watch the approach and walkthrough videos first! """

def find(roots, a):
  if roots[a] == a:
    return a
  return find(roots, roots[a])

def union(roots, a, b):
  root_a = find(roots, a)
  root_b = find(roots, b)
  if root_a == root_b:
    return
  roots[root_b] = root_a

def count_components(n, edges):
  roots = []

  for i in range(n):
    roots.append(i)
  
  for edge in edges:
    a, b = edge
    union(roots, a, b)

  count = 0
  for i in range(0, len(roots)):
    if i == roots[i]:
      count += 1
  return count

count_components(7, [
  (0, 2),
  (1, 0),
  (4, 3),
  (2, 5),
  (3, 6)
]) # -> 2