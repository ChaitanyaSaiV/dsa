""" longest path
Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. 
A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes. """


def longest_path(graph):
  distance = {}
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0
      
  for node in graph:
    traverse_distance(graph, node, distance)
    
  return max(distance.values())

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
  
  largest = 0
  for neighbor in graph[node]:
    attempt = traverse_distance(graph, neighbor, distance)
    if attempt > largest:
      largest = attempt
  
  distance[node] = 1 + largest
  return distance[node]


        
      


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