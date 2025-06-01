from collections import deque
def closest_carrot(grid, starting_row, starting_col):
  visited = set()
  queue = deque([(starting_row, starting_col, 0)])

  while queue:
    r , c , distance = queue.popleft()

    if grid[r][c] == 'C':
      return distance

    positions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for position in positions:
      delta_row, delta_col = position
      row_pos = r + delta_row
      row_col = c + delta_col

      row_bound = 0 <= row_pos < len(grid)
      col_bound = 0 <= row_col < len(grid[0])

      pos = (row_pos, row_col)
      if row_bound and col_bound and pos not in visited and grid[row_pos][row_col] != 'X':
        queue.append((row_pos, row_col, distance + 1))
        visited.add(pos)

  return -1



grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

closest_carrot(grid, 1, 2)