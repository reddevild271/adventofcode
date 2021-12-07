from sys import stdin
from collections import Counter

fishes = Counter((int(x) for x in stdin.readline().split(',')))

def fish_exp(timer, days):
  if timer >= days:
    return 1
  return fish_exp(6, days-timer-1) + fish_exp(8, days-timer-1)

total_fish = 0
for timer, count in fishes.items():
  total_fish += fish_exp(timer, 80) * count

print(total_fish)
