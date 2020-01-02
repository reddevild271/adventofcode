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
right = []
left = []
xPosDict = {}
xNegDict = {}

for a in asteroids:
  aright = []
  aleft = []
  xPositive = {}
  xNegative = {}
  count = 0
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
        if f not in xPositive:
          xPositive[f] = [a2]
          count += 1
        else:
          xPositive[f].append(a2)
      except:
        if not zeroYposFound:
          count += 1
          zeroYposFound = True
        aright.append(a2)
    else:
      try:
        f = Fraction(xDif,yDif)
        if f not in xNegative:
          xNegative[f] = [a2]
          count += 1
        else:
          xNegative[f].append(a2)
      except:
        if not zeroYnegFound:
          count += 1
          zeroYnegFound = True
        aleft.append(a2)
  if count > maxCount:
    maxCount = count
    maxLoc = a
    xPosDict = xPositive
    xNegDict = xNegative
    right = aright
    left = aleft

for x in xPosDict:
  xPosDict[x] = sorted(xPosDict[x], key=lambda y: y[0]-maxLoc[0])
for x in xNegDict:
  xNegDict[x] = sorted(xNegDict[x], key=lambda y: maxLoc[0]-y[0])

right = sorted(right, key=lambda y: y[0]-maxLoc[0])
left = sorted(left, key=lambda y: maxLoc[0]-y[0])

sortedPosDict = sorted(xPosDict)
sortedNegDict = sorted(xNegDict)[::-1]

sortList1 = [x for x in sortedPosDict if x >= 0][::-1]
sortList2 = [x for x in sortedPosDict if x < 0][::-1]
sortList3 = [x for x in sortedNegDict if x >= 0][::-1]
sortList4 = [x for x in sortedNegDict if x < 0][::-1]

#print(sortList1)
#print(right)
#print(sortList2)
#print(sortList3)
#print(left)
#print(sortList4)

i = 0
while i < 200:
  for s in sortList2:
    if len(xPosDict[s]):
      i += 1
      print(s)
      print("i="+str(i))
      #print(xPosDict[s][0])
      if i == 200:
        print(xPosDict[s][0])
        break
      xPosDict[s] = xPosDict[s][1:]
  if len(right):
    i += 1
    print("right")
    print("i="+str(i))
    #print(right[0])
    if i == 200:
        print(right[0])
        break
    right = right[1:]
  for s in sortList1:
    if len(xPosDict[s]):
      i += 1
      print(s)
      print("i="+str(i))
      #print(xPosDict[s][0])
      if i == 200:
        print(xPosDict[s][0])
        break
      xPosDict[s] = xPosDict[s][1:]
  for s in sortList3:
    if len(xNegDict[s]):
      i += 1
      print(s)
      print("i="+str(i))
      #print(xNegDict[s][0])
      if i == 200:
        print(xNegDict[s][0])
        break
      xNegDict[s] = xNegDict[s][1:]
  if len(left):
    i += 1
    print(left)
    print("i="+str(i))
    #print(left[0])
    if i == 200:
        print(left[0])
        break
    left = left[1:]
  for s in sortList4:
    if len(xNegDict[s]):
      i += 1
      print(s)
      print("i="+str(i))
      #print(xNegDict[s][0])
      if i == 200:
        print(xNegDict[s][0])
        break
      xNegDict[s] = xNegDict[s][1:]
