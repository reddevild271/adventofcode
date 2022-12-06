from sys import stdin

overlap = 0
for line in stdin:
  a, b = [[int(y) for y in x] for x in [r.split('-') for r in line[:-1].split(',')]]
  if max(a[0], b[0]) <= min(a[1], b[1]):
    overlap += 1

print(overlap)
