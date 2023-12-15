from sys import stdin

def HASH(s):
  current_value = 0
  for c in s:
    current_value += ord(c)
    current_value *= 17
    current_value %= 256
  return current_value

labels = [[] for i in range(256)]
lenses = [[] for i in range(256)]

init_seq = stdin.read()[:-1].split(',')
for step in init_seq:
  if '=' in step:
    label, lens = step.split('=')
    box_idx = HASH(label)
    try:
      label_idx = labels[box_idx].index(label)
      lenses[box_idx][label_idx] = int(lens)
    except ValueError:
      labels[box_idx].append(label)
      lenses[box_idx].append(int(lens))
    continue
  label = step[:-1]
  box_idx = HASH(label)
  try:
    label_idx = labels[box_idx].index(label)
    del labels[box_idx][label_idx]
    del lenses[box_idx][label_idx]
  except ValueError:
    continue

total = 0
for i in range(len(lenses)):
  for j, lens in enumerate(lenses[i]):
    total += (i + 1) * (j + 1) * lens
print(total)
