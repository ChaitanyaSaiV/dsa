""" knight attack
A knight and a pawn are on a chess board. Can you figure out the minimum number of moves required for the knight to travel to the same position of the pawn? 

On a single move, the knight can move in an "L" shape; two spaces in any direction, then one space in a perpendicular direction. This means that on a single move, a knight has eight possible positions it can move to.

Write a function, knight_attack, that takes in 5 arguments:

n, kr, kc, pr, pc

n = the length of the chess board
kr = the starting row of the knight
kc = the starting column of the knight
pr = the row of the pawn
pc = the column of the pawn
The function should return a number representing the minimum number of moves required for the knight to land ontop of the pawn. The knight cannot move out-of-bounds of the board. 

You can assume that rows and columns are 0-indexed. This means that if n = 8, there are 8 rows and 8 columns numbered 0 to 7. If it is not possible for the knight to attack the pawn, then return None.
 """

from collections import deque

def knight_attack(n, kr, kc, pr, pc):
  queue = deque([(kr, kc, 0)])
  visited = {(kr,kc)}

  while len(queue) > 0:
    r, c, level = queue.popleft()
    if r == pr and c == pc:
      return level
    
    visited.add((r, c))

    positons = get_positions(n, r, c)

    for position in positons:
      if position not in visited:
        r, c = position
        queue.append((r, c, level + 1))
    
  return None



def get_positions(n, kr, kc):
  positions = [
    (kr + 2, kc + 1),
    (kr - 2, kc + 1),
    (kr + 2, kc - 1),
    (kr - 2, kc - 1),
    (kr + 1, kc + 2),
    (kr - 1, kc + 2),
    (kr + 1, kc - 2),
    (kr - 1, kc - 2)
  ]
  possible_positions = []
  for position in positions:
    r, c = position
    if 0 <= r <= (n - 1) and 0 <= c <= (n - 1):
      possible_positions.append[(r, c)]

  return possible_positions


knight_attack(8, 1, 1, 2, 2) # -> 2