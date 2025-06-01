def minimum_island(grid):
  visited = set()

  min = float("inf")

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      count = explore(grid, r, c, visited)
      if count < min and count > 0:
        min = count

  return min


def explore(grid, r, c, visited):
  range_r = 0 <= r < len(grid)
  range_c = 0 <= c < len(grid[0])

  if not range_r or not range_c:
    return 0
  pos = (r, c)

  if pos in visited:
    return 0
  
  if grid[r][c] == 'W':
    return 0
  
  visited.add(pos)

  sum = 1

  sum += explore(grid, r - 1, c, visited)
  sum += explore(grid, r + 1, c, visited)
  sum += explore(grid, r, c - 1, visited)
  sum += explore(grid, r, c + 1, visited)

  return sum


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

minimum_island(grid) # -> 2