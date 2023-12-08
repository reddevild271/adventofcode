from sys import stdin

class Instructions:
  index = 0
  s = ''

  def next_inst(self):
    ret = self.s[self.index]
    self.index = (self.index + 1) % len(self.s)
    return ret

class Node:
  s = ''
  left = None
  right = None

class RepeatGroup:
  repeats = None
  increment = 0

  def is_z(self, step):
    for rep in self.repeats:
      while rep < step:
        rep += self.increment
      if rep == step:
        return True
    return False

insts = None
node_dict = {}
path_nodes = []

for line in stdin:
  if insts is None:
    insts = Instructions()
    insts.s = line[:-1]
    continue
  if len(line) == 1:
    continue
  start = line[0:3]
  if start not in node_dict:
    node_start = Node()
    node_start.s = start
    node_dict[start] = node_start
  node = node_dict[start]
  left = line[7:10]
  if left not in node_dict:
    node_left = Node()
    node_left.s = left
    node_dict[left] = node_left
  node.left = node_dict[left]
  right = line[12:15]
  if right not in node_dict:
    node_right = Node()
    node_right.s = right
    node_dict[right] = node_right
  node.right = node_dict[right]
  if start[2] == 'A':
    path_nodes.append(node)

groups = []

for node in path_nodes:
  steps = 0
  track_nodes = [[] for i in insts.s]
  track_steps = [[] for i in insts.s]
  repeat_group = RepeatGroup()
  repeat_group.repeats = []
  insts.index = 0
  while node not in track_nodes[insts.index]:
    track_nodes[insts.index].append(node)
    track_steps[insts.index].append(steps)
    if node.s[2] == 'Z':
      repeat_group.repeats.append(steps)
    if insts.next_inst() == 'L':
      node = node.left
    else:
      node = node.right
    steps += 1
  start = track_steps[insts.index][track_nodes[insts.index].index(node)]
  while repeat_group.repeats[0] < start:
    del repeat_group.repeats[0]
  repeat_group.increment = steps - start
  groups.append(repeat_group)

print([g.repeats for g in groups])

steps = 0
incr = min(g.increment for g in groups)
while not all(g.is_z(steps) for g in groups):
  steps += incr
print(steps)
