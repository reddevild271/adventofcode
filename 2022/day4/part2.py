from sys import stdin

overlap = 0
for line in stdin:
  range_a, range_b = line[:-1].split(',')
  a_min, a_max = [int(x) for x in range_a.split('-')]
  b_min, b_max = [int(x) for x in range_b.split('-')]
  max_min = max(a_min, b_min)
  min_max = min(a_max, b_max)
  if max_min <= min_max:
    overlap += 1

print(overlap)
