from sys import stdin

def in_bounds(xy, cave, mult=5):
  x,y = xy
  return x in range(len(cave[0])*mult) and \
         y in range(len(cave)*mult)

def risk_level(xy, cave):
  x,y = xy
  risk = cave[x%len(cave[0])][y%len(cave)]
  risk += x//len(cave[0]) + y//len(cave)
  while risk > 9:
    risk -= 9
  return risk

cave = [[int(risk) for risk in line[:-1]] for line in stdin]

found = {}
paths = [((0,0),0)]
mult = 5

while len(paths) > 0:
  path = paths[0]
  paths = paths[1:]
  paths.sort(key = lambda p: p[1])
  if not in_bounds(path[0], cave):
    continue
  total_risk = path[1] + risk_level(path[0],cave)
  if (len(cave[0])*mult-1,len(cave)*mult-1) in found:
    if total_risk >= found[(len(cave[0])*mult-1,len(cave)*mult-1)]:
      continue
  if path[0] not in found or total_risk < found[path[0]]:
    found[path[0]] = total_risk
    paths.append(((path[0][0]+1,path[0][1]),total_risk))
    paths.append(((path[0][0],path[0][1]+1),total_risk))
    paths.append(((path[0][0]-1,path[0][1]),total_risk))
    paths.append(((path[0][0],path[0][1]-1),total_risk))

print(found[(len(cave[0])*mult-1,len(cave)*mult-1)]-cave[0][0])
    
