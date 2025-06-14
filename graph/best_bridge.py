""" best bridge
Write a function, best_bridge, that takes in a grid as an argument. The grid contains water (W) and land (L). There are exactly two islands in the grid. An island is a vertically or horizontally connected region of land. Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line. """

from collections import deque

def best_bridge(grid):
  island = first_island(grid)
  return find_bridge(grid, island)

def find_bridge(grid, first_island):
  visited = set()
  queue = deque()
  for island in first_island:
    queue.append((island, 0))
  bounds = [(0,1), (0,-1), (1,0), (-1,0)]
  while queue:
    pos, length = queue.popleft()
    r, c = pos
    if grid[r][c] == 'L' and pos not in first_island:
      return length - 1
    visited.add(pos)
    for bound in bounds:
      i, j = bound
      current_r = r + i
      current_c = c + j
      pos = (current_r, current_c)
      if bound_check(grid, current_r, current_c) and pos not in visited:
        pos = (current_r, current_c)
        queue.append((pos, length + 1))



def first_island(grid):
  island = set()
  for i in range(0, len(grid)):
    if len(island) > 0:
      break
    for j in range(0, len(grid[0])):
      if bound_check(grid, i, j):
        if grid[i][j] == 'L':
          r = i
          c = j
          island.add((r,c))
          break

  queue = deque([(r,c)])
  
  bounds = [(0,1), (0,-1), (1,0), (-1,0)]

  while queue:
    r, c = queue.popleft()
    for bound in bounds:
      i, j = bound
      current_r = r + i
      current_c = c + j
      if bound_check(grid, current_r, current_c):
        if grid[current_r][current_c] == 'L' and (current_r, current_c) not in island:
          queue.append((current_r, current_c))
          island.add((current_r, current_c))

  return island

def bound_check(grid, r, c):
  if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
    return True
  return False



grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
best_bridge(grid) # -> 1