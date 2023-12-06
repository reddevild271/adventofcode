from sys import stdin
from math import sqrt, ceil

times = []
distances = []
for line in stdin:
  if not times:
    times = [int(x) for x in line.split(':')[1].split()]
    continue
  if not distances:
    distances = [int(x) for x in line.split(':')[1].split()]

total = 1
for time, dist in zip(times, distances):
  sqrt_disc_2 = sqrt( time * time - 4 * dist ) / 2
  t_2 = time / 2
  total *= ceil(t_2 + sqrt_disc_2) - int(t_2 - sqrt_disc_2) - 1

print(total)
