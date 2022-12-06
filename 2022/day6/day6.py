line = input()

found = False
i = 0
while not found:
  if len(set(line[i:i+4])) == 4:
    found = True
  else:
    i += 1
print(f'Part 1: {i + 4}')
  
found = False
i = 0
while not found:
  if len(set(line[i:i+14])) == 14:
    found = True
  else:
    i += 1
print(f'Part 2: {i + 14}')
