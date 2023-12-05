from sys import stdin

class MapRange:
  dst = 0
  src = 0
  rng = 0
  
  def __lt__(self, other):
    return self.dst < other.dst

class SeedRange:
  start = 0
  length = 0
  
  def __lt__(self, other):
    return self.start < other.start

def loc_to_seed(loc, maps, seeds):
  for m in maps[::-1]:
    for m_r in m:
      if loc >= m_r.dst + m_r.rng:
        break
      if loc >= m_r.dst:
        loc = m_r.src + loc - m_r.dst
        break
  for s_r in seeds:
    if loc >= s_r.start + s_r.length:
      break
    if loc >= s_r.start:
      return loc
  return None
      
state = 0

seeds = []
maps = []
minimum_range = None
for line in stdin:
  if not seeds:
    tmp_seeds = [int(x) for x in line.split(':')[1].split()]
    for start, length in zip(tmp_seeds[::2], tmp_seeds[1::2]):
      seed_range = SeedRange()
      seed_range.start = start
      seed_range.length = length
      seeds.append(seed_range)
    seeds.sort(reverse=True)
    minimum_range = min([s_r.length for s_r in seeds])
    continue
  if len(line) == 1:
    if maps:
      maps[-1].sort(reverse=True)      
    maps.append([])
    state = 0
    continue
  if state == 0:
    state = 1
    continue
  map_range = MapRange()
  map_range.dst, map_range.src, map_range.rng = [int(x) for x in line.split()]
  maps[-1].append(map_range)
  minimum_range = min(map_range.rng, minimum_range)

location = 0
while True:
  seed = loc_to_seed(location, maps, seeds)
  if seed is not None:
    break
  location += minimum_range

found = False
for i in range(location - minimum_range + 1, location):
  seed = loc_to_seed(i, maps, seeds)
  if seed is not None:
    print(i)
    exit()

print(location)
