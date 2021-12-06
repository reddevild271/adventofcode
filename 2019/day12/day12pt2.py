from itertools import combinations

class Planet:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.dx = 0
    self.dy = 0
    self.dz = 0
  def gravityX(self, p):
    if p.x > self.x:
      self.dx += 1
      p.dx -= 1
    elif p.x < self.x:
      self.dx -= 1
      p.dx += 1
  def velocityX(self):
    self.x += self.dx
  def __str__(self):
    return "<x="+str(self.x)+">"
  def __iter__(self):
    yield self.x
    yield self.y
    yield self.z
    yield self.dx
    yield self.dy
    yield self.dz

planets = [Planet(-5,6,-11),
           Planet(-8,-4,-2),
           Planet(1,16,4),
           Planet(11,11,-4)]

p0XDict = {tuple(planets[0]):[0]}

planetCombos = list(combinations(planets,2))

i = 0
while i < 1000000:
  i += 1
  for pc in planetCombos:
    pc[0].gravityX(pc[1])
  for p in planets:
    p.velocityX()
  if tuple(planets[0]) not in p0XDict:
    p0XDict[tuple(planets[0])] = []
  p0XDict[tuple(planets[0])].append(i)

s = sorted(p0XDict, key=lambda x: len(p0XDict[x]))
print(s[-1])
print(p0XDict[s[-1]])
  
  
  
