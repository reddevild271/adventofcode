from sys import stdin

elf_count = 0
current_set = {}
priorities = 0
for line in stdin:
  elf_count += 1
  if elf_count == 1:
    current_set = set(line[:-1])
  else:
    current_set = current_set.intersection(line[:-1])
  if elf_count == 3:
    same_item = ord(list(current_set)[0])
    if same_item > 96:
      priorities += same_item - 96
    else:
      priorities += same_item - 38
    elf_count = 0

print(priorities)
