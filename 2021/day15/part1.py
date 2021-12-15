from sys import stdin

cave = [[int(risk) for risk in line[:-1]] for line in stdin]

found = {}
paths = [((0,0),0)]

while len(paths) > 0:
  path = paths[0]
  paths = paths[1:]
  paths.sort(key = lambda p: p[1])
  if path[0][0] not in range(len(cave[0])) or \
     path[0][1] not in range(len(cave)):
    continue
  total_risk = path[1] + cave[path[0][0]][path[0][1]]
  if (len(cave[0])-1,len(cave)-1) in found:
    if total_risk >= found[(len(cave[0])-1,len(cave)-1)]:
      continue
  if path[0] not in found or total_risk < found[path[0]]:
    found[path[0]] = total_risk
    paths.append(((path[0][0]+1,path[0][1]),total_risk))
    paths.append(((path[0][0],path[0][1]+1),total_risk))
    paths.append(((path[0][0]-1,path[0][1]),total_risk))
    paths.append(((path[0][0],path[0][1]-1),total_risk))

print(found[(len(cave[0])-1,len(cave)-1)]-cave[0][0])
    
