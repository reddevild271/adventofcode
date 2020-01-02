from sys import stdin
from operator import itemgetter

wire1 = [(x[0],int(x[1:])) for x in stdin.readline().split(',')]
wire2 = [(x[0],int(x[1:])) for x in stdin.readline().split(',')]

x = 0
y = 0
steps = 0

pathPoints = {}

for step in wire1:
  xstep = 0
  ystep = 0
  if step[0] == 'U':
    ystep = 1
  elif step[0] == 'D':
    ystep = -1
  elif step[0] == 'R':
    xstep = 1
  else:
    xstep = -1
  for i in range(step[1]):
    x += xstep
    y += ystep
    steps += 1
    if (x,y) in pathPoints:
      continue
    pathPoints[(x,y)] = steps

x = 0
y = 0
steps = 0

minDist = -1

for step in wire2:
  xstep = 0
  ystep = 0
  if step[0] == 'U':
    ystep = 1
  elif step[0] == 'D':
    ystep = -1
  elif step[0] == 'R':
    xstep = 1
  else:
    xstep = -1
  for i in range(step[1]):
    x += xstep
    y += ystep
    steps += 1
    if (x,y) in pathPoints:
      totDist = pathPoints[(x,y)] + steps
      if minDist == -1:
        minDist = totDist
      elif minDist > totDist:
        minDist = totDist
      elif steps >= minDist:
        break

print(minDist)
