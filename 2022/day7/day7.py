from sys import stdin
from enum import Enum

State = Enum('State', ['INPUT', 'OUTPUT'])

class Directory:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
    self.files = {}
    self.dirs = {}

  def getSize(self):
    total = 0
    for file in self.files:
      total += self.files[file]
    for d in self.dirs:
      total += self.dirs[d].getSize()
    return total

root_dir = Directory('/', None)
cur_dir = root_dir
all_dirs = [root_dir]

loop_state = State.INPUT

for line in stdin:
  line = line.split()
  if loop_state == State.OUTPUT:
    if line[0] == '$':
      loop_state = State.INPUT
    elif line[0] == 'dir':
      if line[1] not in cur_dir.dirs:
        all_dirs.append(Directory(line[1], cur_dir))
        cur_dir.dirs[line[1]] = all_dirs[-1]
    else:
      if line[1] not in cur_dir.files:
        cur_dir.files[line[1]] = int(line[0])
  if loop_state == State.INPUT:
    if line[1] == 'cd':
      if line[2] == '/':
        cur_dir = root_dir
      elif line[2] == '..':
        if cur_dir.parent:
          cur_dir = cur_dir.parent
      else:
        cur_dir = cur_dir.dirs[line[2]]
    elif line[1] == 'ls':
      loop_state = State.OUTPUT

total = 0
for d in all_dirs:
  sz = d.getSize()
  if sz <= 100000:
    total += sz
print(f'Part 1: {total}')

space_needed = root_dir.getSize() - 40000000
candidates = []
for d in all_dirs:
  sz = d.getSize()
  if sz >= space_needed:
    candidates.append(sz)
candidates.sort()
print(f'Part 2: {candidates[0]}')
