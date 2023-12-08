from sys import stdin

class Instructions:
  index = 0
  s = ''

  def next_inst(self):
    ret = self.s[self.index]
    self.index = (self.index + 1) % len(self.s)
    return ret

insts = None
nodes_left = {}
nodes_right = {}

for line in stdin:
  if insts is None:
    insts = Instructions()
    insts.s = line[:-1]
    continue
  if len(line) == 1:
    continue
  start = line[0:3]
  nodes_left[start] = line[7:10]
  nodes_right[start] = line[12:15]

node = 'AAA'
steps = 0
while node != 'ZZZ':
  next_step = insts.next_inst()
  if next_step == 'L':
    node = nodes_left[node]
  else:
    node = nodes_right[node]
  steps += 1

print(steps)
