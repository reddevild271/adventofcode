from sys import stdin

class MapRange:
  dst = 0
  src = 0
  rng = 0

state = 0

seeds = []
maps = []
for line in stdin:
  if not seeds:
    seeds = [int(x) for x in line.split(':')[1].split()]
    continue
  if len(line) == 1:
    maps.append([])
    state = 0
    continue
  if state == 0:
    state = 1
    continue
  map_range = MapRange()
  map_range.dst, map_range.src, map_range.rng = [int(x) for x in line.split()]
  maps[-1].append(map_range)

min_location = None
for seed in seeds:
  for m in maps:
    for m_r in m:
      if seed >= m_r.src and seed < m_r.src + m_r.rng:
        seed = m_r.dst + seed - m_r.src
        break
  if min_location == None:
    min_location = seed
  else:
    min_location = min(seed, min_location)

print(min_location)
      
