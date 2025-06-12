""" minimum island
Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island. """


def minimum_island(grid):
  visited = set()
  min_count = float("inf")
  i = 0
  j = 0
  for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
      count = explore_islands(grid, visited, i, j)
      if count > 0 and count < min_count:
        min_count = count
      
  return min_count

def explore_islands(grid, visited, i, j):

  count = 1

  coordinates = (i,j)

  row_bound = 0 <= i < len(grid)
  coulmn_bound = 0 <= j < len(grid[0])

  if not row_bound or not coulmn_bound:
    return 0
  

  if coordinates in visited:
    return 0
  else:
    visited.add(coordinates)

  if grid[i][j] == 'W':
    return 0
  
  count += explore_islands(grid, visited, i + 1, j)
  count += explore_islands(grid, visited, i - 1, j)
  count += explore_islands(grid, visited, i, j + 1)
  count += explore_islands(grid, visited, i, j - 1)

  return count


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

minimum_island(grid) 