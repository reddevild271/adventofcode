from sys import stdin

points = {}

for line in stdin:
  a,b,c = line.split()
  x1, y1 = [int(x) for x in a.split(',')]
  x2, y2 = [int(x) for x in c.split(',')]

  inc_x = 0
  if x2 - x1 > 0:
    inc_x = 1
  elif x2 - x1 < 0:
    inc_x = -1

  inc_y = 0
  if y2 - y1 > 0:
    inc_y = 1
  elif y2 - y1 < 0:
    inc_y = -1

  while x1 != x2 + inc_x or y1 != y2 + inc_y:
    if (x1,y1) not in points:
      points[(x1,y1)] = 1
    else:
      points[(x1,y1)] += 1
    x1 += inc_x
    y1 += inc_y    

print(sum(value > 1 for value in points.values()))
