from sys import stdin

cave = {}

for line in stdin:
  begin, end = line[:-1].split('-')
  if begin in cave:
    cave[begin].append(end)
  else:
    cave[begin] = [end]
  if end in cave:
    cave[end].append(begin)
  else:
    cave[end] = [begin]

def cave_paths(cave, node, prev, twice):
  if node == 'end':
    return 1
  if node.islower():
    if node in prev:
      if twice or node == 'start':
        return 0
      twice = True
    prev.append(node)
  paths = 0
  for n in cave[node]:
    paths += cave_paths(cave, n, prev[:], twice)
  return paths

print( cave_paths(cave, 'start', [], False) )
