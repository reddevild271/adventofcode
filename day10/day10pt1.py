from sys import stdin
from fractions import Fraction

grid = []
asteroids = []
row = 0

for line in stdin:
  grid.append(line[:-1])
  col = 0
  for pt in line:
    if pt == '#':
      asteroids.append((col,row))
    col += 1
  row += 1

maxCount = 0
maxLoc = (0,0)

for a in asteroids:
  xPositive = set()
  xNegative = set()
  count = 0
  zeroYposFound = False
  zeroYnegFound = False
  for a2 in asteroids:
    if a == a2:
      continue
    xDif = a2[0]-a[0]
    yDif = a2[1]-a[1]
    if xDif > 0 or xDif == 0 and yDif >= 0:
      try:
        f = Fraction(xDif,yDif)
        if f not in xPositive:
          xPositive.add(f)
          count += 1
      except:
        if not zeroYposFound:
          count += 1
          zeroYposFound = True
    else:
      try:
        f = Fraction(xDif,yDif)
        if f not in xNegative:
          xNegative.add(f)
          count += 1
      except:
        if not zeroYnegFound:
          count += 1
          zeroYnegFound = True
  if count > maxCount:
    maxCount = count
    maxLoc = a

print(maxCount)
