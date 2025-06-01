def best_bridge(grid):
  visited = set()

  min_count = float("inf")

  for r in range (len(grid)):
    for c in range (len(grid[0])):
      if explore(grid, r, c, visited) == True:
        island = calculate_bridge(grid, visited)
        for node in visited:
          row, col = node




  return min_count

def find_land(grid, r, c, visited):
  row_bound = 0 <= r < len(grid)
  col_bound = 0 <= c < len(grid[0])
  if not row_bound or not col_bound:
    return
  
  if grid[r][c] == 'W':
    return

  if pos in visited:
    return

def explore(grid, r, c, visited):
  row_bound = 0 <= r < len(grid)
  col_bound = 0 <= c < len(grid[0])
  if not row_bound or not col_bound:
    return
  if grid[r][c] == 'W':
    return
  
  pos = (r, c)

  if pos in visited:
    return

  visited.add(pos)

  explore(grid, r - 1, c, visited)
  explore(grid, r + 1, c, visited)
  explore(grid, r, c - 1, visited)
  explore(grid, r, c + 1, visited)
  return True



grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
best_bridge(grid)