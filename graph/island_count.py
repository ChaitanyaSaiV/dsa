""" island count
Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.
 """



def island_count(grid):
  visited = set()
  count = 0
  i = 0
  j = 0
  for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
      if explore_islands(grid, visited, i, j):
        count += 1
  return count

def explore_islands(grid, visited, i, j):

  

  coordinates = (i,j)

  row_bound = 0 <= i < len(grid)
  coulmn_bound = 0 <= j < len(grid[0])

  if not row_bound or not coulmn_bound:
    return False
  

  if coordinates in visited:
    return False
  else:
    visited.add(coordinates)

  if grid[i][j] == 'W':
    return False
  
  explore_islands(grid, visited, i + 1, j)
  explore_islands(grid, visited, i - 1, j)
  explore_islands(grid, visited, i, j + 1)
  explore_islands(grid, visited, i, j - 1)
  return True


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

island_count(grid) # -> 3