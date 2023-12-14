from sys import stdin

area = []

for line in stdin:
  area.append(list(line[:-1]))

for y, row in enumerate(area):
  if y == 0:
    continue
  for x, c in enumerate(row):
    i = 1
    if c == 'O':
      while y - i >= 0 and area[y-i][x] == '.':
        area[y-i][x] = 'O'
        area[y-i+1][x] = '.'
        i += 1

total = 0
for i, row in enumerate(area[::-1]):
  total += row.count('O') * (i+1)
print(total)
