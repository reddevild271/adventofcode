from sys import stdin

total = 0
for line in stdin:
  game, moves = line.split(':')
  moves = moves[1:-1].split()
  valid = True
  for num, color in zip(moves[::2],moves[1::2]):
    n = int(num)
    c = color[0]
    if n > 14 or n == 14 and c != 'b' or n == 13 and c == 'r':
      valid = False
      break
  if valid:
    total += int(game.split(' ')[1])
print(total)
      
