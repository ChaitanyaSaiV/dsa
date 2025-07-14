""" string search
Write a function, string_search, that takes in a grid of letters and a string as arguments. 

The function should return a boolean indicating whether or not the string can be found in the grid as a path by connecting horizontal or vertical positions. 

The path can begin at any position, but you cannot reuse a position more than once in the path.

You can assume that all letters are lowercase and alphabetic. """


def string_search(grid, s):

  counter = len(s)

  pos = 0
  
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == s[pos]:
        if validate_surroundings(grid, i, j, 0, s) == True:
          return True

  return False

def validate_surroundings(grid, r, c, pos, s):
  if pos > len(s) - 1:
    return True

  if pos != 0 and grid[r][c] != s[pos]:
    return False
  
  coordinates = get_coordinates(grid, r, c)

  for coordinate in coordinates:
    a, b = coordinate
    if validate_surroundings(grid, a, b, pos + 1, s):
      return True
  
  return False

def get_coordinates(grid, r , c):
  inbound_positions = []

  positions = [
    (r - 1, c),
    (r + 1, c),
    (r, c + 1),
    (r, c - 1)
  ]

  for pos in positions:
    a , c = pos

    if 0 <= a < len(grid) and 0 <= c < len(grid[0]):
      inbound_positions.append(pos)

  return inbound_positions
  
grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'c', 'm']
]
print(string_search(grid, 'hello')) # -> True