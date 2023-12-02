from sys import stdin

total = 0
for line in stdin:
  d = { 'r': 0, 'g': 0, 'b': 0 }
  game, moves = line.split(':')
  moves = moves[1:-1].split()
  for num, color in zip(moves[::2],moves[1::2]):
    d[color[0]] = max(int(num), d[color[0]])
  total += d['r'] * d['g'] * d['b']
  
print(total)
      
