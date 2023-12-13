from sys import stdin

def diff(r1, r2):
  d = 0
  for a, b in zip(r1, r2):
    d += 0 if a == b else 1
    if d > 1:
      return d
  return d

def reflect(p):
  for i in range(len(p) - 1):
    inc = 0
    tot_diff = 0
    while i - inc >= 0 and i + 1 + inc < len(p):
      tot_diff += diff(p[i - inc], p[i + 1 + inc])
      if tot_diff > 1:
        break
      inc += 1
    else:
      if tot_diff == 1:
        return i + 1
  return 0

pattern = [[]]
for line in stdin:
  if len(line) > 1:
    pattern[-1].append(list(line[:-1]))
    continue
  pattern.append([])

total = 0
for p in pattern:
  ref = reflect(p)
  if ref:
    total += 100 * ref
    continue
  p_rot = [[row[i] for row in p] for i in range(len(p[0]))]
  total += reflect(p_rot)

print(total)
