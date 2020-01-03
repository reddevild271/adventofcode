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

maxCount = 278
a = maxLoc = (23,19)
right = []
left = []
xPosDict = {}
xNegDict = {}

zeroYposFound = False
zeroYnegFound = False
for a2 in asteroids:
  if a == a2:
    continue
  xDif = a2[0]-a[0]
  yDif = a2[1]-a[1]
  if xDif > 0 or xDif == 0 and yDif < 0:
    try:
      f = Fraction(xDif,yDif)
      if f not in xPosDict:
        xPosDict[f] = []
      xPosDict[f].append(a2)
    except:
      zeroYposFound = True
      right.append(a2)
  else:
    try:
      f = Fraction(xDif,yDif)
      if f not in xNegDict:
        xNegDict[f] = []
      xNegDict[f].append(a2)
    except:
      zeroYnegFound = True
      left.append(a2)

# sort linear asteroids
for x in xPosDict:
  xPosDict[x] = sorted(xPosDict[x], key=lambda y: abs(y[1]-maxLoc[1]))
for x in xNegDict:
  xNegDict[x] = sorted(xNegDict[x], key=lambda y: abs(y[1]-maxLoc[1]))

right = sorted(right, key=lambda y: y[0]-maxLoc[0])
left = sorted(left, key=lambda y: maxLoc[0]-y[0])

# sort by angle from base
sortedPosDict = sorted(xPosDict)[::-1]
sortedNegDict = sorted(xNegDict)[::-1]

# turn into the 4 quadrants
sortList1 = [x for x in sortedPosDict if x <= 0]
sortList2 = [x for x in sortedPosDict if x > 0]
sortList3 = [x for x in sortedNegDict if x <= 0]
sortList4 = [x for x in sortedNegDict if x > 0]

# go through each quadrant clockwise
i = 0
state = 0
while i < 200:
  if state == 0:
    for s in sortList1:
      if len(xPosDict[s]):
        i += 1
        if i == 200:
          print(xPosDict[s][0])
          break
        xPosDict[s] = xPosDict[s][1:]
  elif state == 1:
    if len(right):
      i += 1
      if i == 200:
        print(right[0])
        break
      right = right[1:]
  elif state == 2:
    for s in sortList2:
      if len(xPosDict[s]):
        i += 1
        if i == 200:
          print(xPosDict[s][0])
          break
        xPosDict[s] = xPosDict[s][1:]
  elif state == 3:
    for s in sortList3:
      if len(xNegDict[s]):
        i += 1
        if i == 200:
          print(xNegDict[s][0])
          break
        xNegDict[s] = xNegDict[s][1:]
  elif state == 4:
    if len(left):
      i += 1
      if i == 200:
        print(left[0])
        break
      left = left[1:]
  elif state == 5:
    for s in sortList4:
      if len(xNegDict[s]):
        i += 1
        if i == 200:
          print(xNegDict[s][0])
          break
        xNegDict[s] = xNegDict[s][1:]
  state = (state+1)%6
