from sys import stdin
from collections import Counter

fishes = Counter((int(x) for x in stdin.readline().split(',')))
for i in range(9):
  if i not in fishes:
    fishes[i] = 0

for i in range(256):
  tmp = fishes[0]
  fishes[0] = fishes[1]
  fishes[1] = fishes[2]
  fishes[2] = fishes[3]
  fishes[3] = fishes[4]
  fishes[4] = fishes[5]
  fishes[5] = fishes[6]
  fishes[6] = fishes[7] + tmp
  fishes[7] = fishes[8]
  fishes[8] = tmp

print(sum(fishes.values()))
