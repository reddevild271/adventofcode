from sys import stdin

crabs = [int(x) for x in stdin.readline().split(',')]

def crab_calc( crabs, pos ):
  return sum([abs(crab-pos) for crab in crabs])

print(min([crab_calc(crabs, pos) for pos in range(min(crabs), max(crabs)+1)]))
