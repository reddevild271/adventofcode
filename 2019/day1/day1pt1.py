from sys import stdin

fuelDict = {}
total = 0

for x in stdin:
  if x in fuelDict:
    total += fuelDict[x]
  else:
    fuel = int(x) // 3 - 2
    fuelDict[x] = fuel
    total += fuel

print(total)
