from sys import stdin

full_overlap = 0
for line in stdin:
  ranges = [[int(y) for y in x] for x in [r.split('-') for r in line[:-1].split(',')]]
  if [min(ranges[0][0], ranges[1][0]), max(ranges[0][1], ranges[1][1])] in ranges:
    full_overlap += 1

print(full_overlap)
