from sys import stdin
from operator import itemgetter

wire1 = [(x[0],int(x[1:])) for x in stdin.readline().split(',')]
wire2 = [(x[0],int(x[1:])) for x in stdin.readline().split(',')]

x = 0
y = 0

pathPoints1 = set()

for step in wire1:
  if step[0] == 'U':
    for i in range(step[1]):
      y += 1
      pathPoints1.add((x,y))
  elif step[0] == 'D':
    for i in range(step[1]):
      y -= 1
      pathPoints1.add((x,y))
  elif step[0] == 'R':
    for i in range(step[1]):
      x += 1
      pathPoints1.add((x,y))
  else:
    for i in range(step[1]):
      x -= 1
      pathPoints1.add((x,y))

x = 0
y = 0

pathPoints2 = set()

for step in wire2:
  if step[0] == 'U':
    for i in range(step[1]):
      y += 1
      pathPoints2.add((x,y))
  elif step[0] == 'D':
    for i in range(step[1]):
      y -= 1
      pathPoints2.add((x,y))
  elif step[0] == 'R':
    for i in range(step[1]):
      x += 1
      pathPoints2.add((x,y))
  else:
    for i in range(step[1]):
      x -= 1
      pathPoints2.add((x,y))

print(sorted([abs(i[0])+abs(i[1]) for i in pathPoints1 & pathPoints2])[0])
