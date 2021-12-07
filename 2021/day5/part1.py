from sys import stdin

points = {}

for line in stdin:
  a,b,c = line.split()
  x1, y1 = [int(x) for x in a.split(',')]
  x2, y2 = [int(x) for x in c.split(',')]

  if x1 == x2:
    ys = sorted((y1, y2))
    for y in range(ys[0],ys[1]+1):
      if (x1,y) not in points:
        points[(x1,y)] = 1
      else:
        points[(x1,y)] += 1
  elif y1 == y2:
    xs = sorted((x1, x2))
    for x in range(xs[0],xs[1]+1):
      if (x,y1) not in points:
        points[(x,y1)] = 1
      else:
        points[(x,y1)] += 1

print(sum(value > 1 for value in points.values()))
