from sys import stdin
from collections import Counter

fishes = Counter((int(x) for x in stdin.readline().split(',')))
for i in range(9):
  if i not in fishes:
    fishes[i] = 0
    
for i in range(256):
  fishes[(i-2)%9] += fishes[i%9]

print(sum(fishes.values()))
