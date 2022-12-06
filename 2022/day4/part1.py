from sys import stdin

full_overlap = 0
for line in stdin:
  range_a, range_b = line[:-1].split(',')
  a_min, a_max = [int(x) for x in range_a.split('-')]
  b_min, b_max = [int(x) for x in range_b.split('-')]
  range_min = min(a_min, b_min)
  range_max = max(a_max, b_max)
  if (range_min, range_max) in ((a_min, a_max),(b_min, b_max)):
    full_overlap += 1

print(full_overlap)
