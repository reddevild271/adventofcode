from sys import stdin

x = 146810
total = 0

while x < 612565:
  y = [c for c in str(x)]
  if y == sorted(str(x)):
    if y[0] == y[1] or y[1] == y[2] or y[2] == y[3] or y[3] == y[4] or y[4] == y[5]:
      total += 1
  x += 1

print(total)
