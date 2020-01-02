from sys import stdin

fuelDict = {-2:0, -1:0, 0:0}
total = 0

def fuelFinder(fuel):
  if fuel in fuelDict:
    return fuelDict[fuel]
  fuelFuel = fuel + fuelFinder( fuel // 3 - 2 )
  fuelDict[fuel] = fuelFuel
  return fuelFuel

for x in stdin:
  total += fuelFinder( int(x) // 3 - 2 )

print(total)
