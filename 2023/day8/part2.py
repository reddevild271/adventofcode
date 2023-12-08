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

z = []

for node in path_nodes:
  steps = 0
  insts.index = 0
  while node.s[2] != 'Z':
    if insts.next_inst() == 'L':
      node = node.left
    else:
      node = node.right
    steps += 1
  z.append(steps // len(insts.s))

total = 1
for p in z:
  total *= p

print(total * len(insts.s))
