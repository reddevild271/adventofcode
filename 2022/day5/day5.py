from sys import stdin
from enum import Enum
from copy import deepcopy

State = Enum('State', ['CRATES', 'NEWLINE', 'MOVES'])
loop_state = State.CRATES

stacks_part1 = {}
stacks_part2 = {}

for line in stdin:
  if loop_state == State.MOVES:
    amount, start, end = [int(x) for x in line.split()[1::2]]
    stacks_part1[end] += stacks_part1[start][-1:-amount-1:-1]
    del stacks_part1[start][-1:-amount-1:-1]
    stacks_part2[end] += stacks_part2[start][-amount:]
    del stacks_part2[start][-amount:]
  elif loop_state == State.CRATES:
    crates = line[1::4]
    if crates[0] == '1':
      loop_state = State.NEWLINE
      stacks_part2 = deepcopy(stacks_part1)
      continue
    for i in range(len(crates)):
      if crates[i] != ' ':
        if i + 1 not in stacks_part1:
          stacks_part1[i+1] = [crates[i]]
        else:
          stacks_part1[i+1] = [crates[i]] + stacks_part1[i+1]
  else: #elif loop_state == State.NEWLINE:
    loop_state = State.MOVES

top_crates = ''
for i in range(len(stacks_part1)):
  top_crates += stacks_part1[i+1][-1]
print(f'Part 1: {top_crates}')

top_crates = ''
for i in range(len(stacks_part2)):
  top_crates += stacks_part2[i+1][-1]
print(f'Part 2: {top_crates}')
