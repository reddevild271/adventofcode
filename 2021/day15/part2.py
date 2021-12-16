from sys import stdin

def in_bounds(xy, cave, mult):
  x,y = xy
  return x >= 0 and x < len(cave[0])*mult and \
         y >= 0 and y < len(cave)*mult

def risk_level(xy, cave):
  x,y = xy
  risk = cave[x%len(cave[0])][y%len(cave)]
  risk += x//len(cave[0]) + y//len(cave)
  return (risk - 1) % 9 + 1

cave = [[int(risk) for risk in line[:-1]] for line in stdin]

found = {}
mult = 5
paths = {(0,0):0}

while len(paths) > 0:
  path = min(paths, key=paths.get)
  new_paths = [(path[0]-1,path[1]), \
               (path[0],path[1]-1), \
               (path[0]+1,path[1]), \
               (path[0],path[1]+1)]
  for new_path in new_paths:
    if in_bounds(new_path, cave, mult) and new_path not in found:
      risk = paths[path] + risk_level(new_path, cave)
      if new_path not in paths:
        paths[new_path] = risk
      else:
        paths[new_path] = min(risk, paths[new_path])
  found[path] = paths[path]
  del paths[path]

print(found[(len(cave[0])*mult-1,len(cave)*mult-1)])
    
