""" province sizes
Write a function, provinceSizes, that takes in a number of cities n and a list of roads which connect cities. 

Roads can be traveled in both directions. Cities are named from 0 to n.

A "province" is a group of 1 or more cities that are connected by roads. The "size" of a province is the number of cities that make up that province.

Your function should return a list containing the sizes of the provinces. You may return the result in any order.

Solve this using Union-Find. """

def find(roots, node):
  if roots[node] == node:
    return node
  
  found = find(roots, roots[node])
  roots[node] = found
  return found

def union(roots, sizes, a, b):
  root_a = find(roots, a)
  root_b = find(roots, b)

  if root_a == root_b:
    return

  if sizes[root_a] >= sizes[root_b]:
    roots[root_b] = root_a
    sizes[root_a] += sizes[root_b]
  else:
    roots[root_a] = root_b
    sizes[root_b] += sizes[root_a]
  return

def province_sizes(n, roads):
  roots = []
  sizes = []

  for i in range(n):
    roots.append(i)
    sizes.append(1)
  
  for road in roads:
    a, b = road
    union(roots, sizes, a, b)
  
  province_size = []
  
  for i in range(n):
    if i == roots[i]:
      province_size.append(sizes[i])
  
  return province_size

province_sizes(6, [
  (4, 5),
  (1, 0),
  (2, 3),
  (0, 5),
  (5, 1),
  (4, 0)
]) # -> [4, 2]