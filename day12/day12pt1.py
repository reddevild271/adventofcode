from itertools import combinations

class Planet:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.dx = 0
    self.dy = 0
    self.dz = 0
  def gravity(self, p):
    if p.x > self.x:
      self.dx += 1
      p.dx -= 1
    elif p.x < self.x:
      self.dx -= 1
      p.dx += 1
    if p.y > self.y:
      self.dy += 1
      p.dy -= 1
    elif p.y < self.y:
      self.dy -= 1
      p.dy += 1
    if p.z > self.z:
      self.dz += 1
      p.dz -= 1
    elif p.z < self.z:
      self.dz -= 1
      p.dz += 1
  def velocity(self):
    self.x += self.dx
    self.y += self.dy
    self.z += self.dz
  def pe(self):
    return abs(self.x)+abs(self.y)+abs(self.z)
  def ke(self):
    return abs(self.dx)+abs(self.dy)+abs(self.dz)
  def te(self):
    return self.pe()*self.ke()
  def __str__(self):
    return "<x="+str(self.x)+", y="+str(self.y)+", z="+str(self.z)+">"

planets = [Planet(-5,6,-11),
           Planet(-8,-4,-2),
           Planet(1,16,4),
           Planet(11,11,-4)]

planetCombos = list(combinations(planets,2))

for step in range(1000):
  for pc in planetCombos:
    pc[0].gravity(pc[1])
  for p in planets:
    p.velocity()

ste = 0
for p in planets:
  ste += p.te()
print(ste)
