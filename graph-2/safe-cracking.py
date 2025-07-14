""" safe cracking

Oh-no! You forgot the number combination that unlocks your safe. 

Luckily, you knew that you'd be forgetful so you previously wrote down a bunch of hints that can be used to determine the correct combination. 

Each hint is a pair of numbers 'x, y' that indicates you must enter digit 'x' before 'y' (but not necessarily immediately before y).

The keypad on the safe has digits 0-9. You can assume that the hints will generate exactly one working combination and that a digit can occur zero or one time in the answer.

Write a function, safe_cracking, that takes in a list of hints as an argument and determines the combination that will unlock the safe. 

The function should return a string representing the combination. """

from collections import deque

def safe_cracking(hints):

  dependency_graph = build_depedency_grap(hints)
  graph = build_graph(hints)

  ready = deque([])

  result = ''

  for hint in dependency_graph:
    if len(dependency_graph[hint]) == 0:
      ready.append(hint)
  
  while len(ready) > 0:
    current = ready.popleft()
    result += str(current)

    for node in graph[current]:
      dependency_graph[node].remove(current)
      if len(dependency_graph[node]) == 0:
        ready.append(node)
  
  return result


def build_depedency_grap(hints):
  graph = {}

  for hint in hints:
    a, b = hint
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    
    graph[b].append(a)

  return graph

def build_graph(hints):
  graph = {}

  for hint in hints:
    a, b = hint

    if a not in graph:
      graph[a] = []

    if b not in graph:
      graph[b] = []
    
    graph[a].append(b)

  return graph


safe_cracking([
  (7, 1),
  (1, 8),
  (7, 8),
]) # -> '718'