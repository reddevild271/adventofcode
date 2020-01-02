from sys import stdin
from collections import deque, defaultdict

orbit_map = defaultdict(list)

for line in stdin:
  x, y = line[:-1].split(')')
  orbit_map[x] += [y]

level_map = [0]*1000
max_level = 0

bfs = deque([('COM',0)])
while len(bfs):
  planet, max_level = bfs.popleft()
  level_map[max_level] += 1
  new_level = max_level + 1
  for p in orbit_map[planet]:
    bfs.append((p,new_level))

print(sum([x*y for x,y in enumerate(level_map)]))
