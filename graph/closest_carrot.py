""" closest carrot
Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column. In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should return a number representing the length of the shortest path from the starting position to a carrot. You may move up, down, left, or right, but cannot pass through walls (X). If there is no possible path to a carrot, then return -1. """


from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  visited = set()
  pos = (starting_row, starting_col)
  queue = deque([(starting_row, starting_col, 0)])

  while queue:
    r, c, length = queue.popleft()

    row_bound_check = 0 <= r < len(grid)
    column_bound_check = 0 <= c < len(grid[0])

    if not row_bound_check or not column_bound_check:
      continue

    pos = (r, c)

    if pos in visited:
      continue

    visited.add(pos)

    if grid[r][c] == 'X':
      continue

    if grid[r][c] == 'C':
      return length
    
    bounds = [(1,0), (-1,0), (0,1), (0,-1)]
    for bound in bounds:
      i, j = bound
      queue.append((r + i, c + j, length + 1))

  return -1
    


grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

closest_carrot(grid, 1, 2) # -> 4