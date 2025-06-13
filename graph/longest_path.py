""" longest path
Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. 
A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes. """


def longest_path(graph):
  visited = {}


  for node in graph:
    explore_path(graph, node, visited)

  return max(visited.values())


def explore_path(graph, node, visited):
  if len(graph[node]) == 0:
    return 0
  if node in visited:
    return visited[node]
  
  length = float("-inf")

  for neighbor in graph[node]:
    neighbor_path = explore_path(graph, neighbor, visited)
    length = max(neighbor_path, length)
  
  length += 1

  visited[node] = length

  return length


        
      


graph = {
  'a': ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'b': ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'c': ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'd': ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'e': ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
  'f': ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'g': ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'h': ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'i': ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
  'j': ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
  'k': ['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
  'l': ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
  'm': ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
  'n': ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
  'o': ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
  'p': ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
  'q': ['r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
  'r': ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
  's': ['t', 'u', 'v', 'w', 'x', 'y', 'z'],
  't': ['u', 'v', 'w', 'x', 'y', 'z'],
  'u': ['v', 'w', 'x', 'y', 'z'],
  'v': ['w', 'x', 'y', 'z'],
  'w': ['x', 'y', 'z'],
  'x': ['y', 'z'],
  'y': ['z'],
  'z': []
}

longest_path(graph)