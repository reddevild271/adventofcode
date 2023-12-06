from sys import stdin
from math import sqrt, ceil

time = 0
distance = 0
for line in stdin:
  if not time:
    time = int(''.join(line.split(':')[1].split()))
    continue
  if not distance:
    distance = int(''.join(line.split(':')[1].split()))

sqrt_disc_2 = sqrt( time * time - 4 * distance ) / 2
t_2 = time / 2
print( ceil(t_2 + sqrt_disc_2) - int(t_2 - sqrt_disc_2) - 1 )
