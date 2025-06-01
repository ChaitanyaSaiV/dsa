def island_count(grid):
  visited = set()

  count = 0

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if explore(grid, r, c, visited) == True:
        count += 1


  return count


def explore(grid, r, c, visited):
  range_r = 0 <= r < len(grid)
  range_c = 0 <= c < len(grid[0])

  if not range_r or not range_c:
    return False
  
  pos = (r, c)

  if grid[r][c] == 'W':
    return False

  if pos in visited:
    return False
  
  visited.add(pos)

  explore(grid, r - 1, c, visited)
  explore(grid, r + 1, c, visited)
  explore(grid, r , c - 1, visited)
  explore(grid, r , c + 1, visited)

  return True

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid))