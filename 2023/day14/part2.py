from sys import stdin

area = []

for line in stdin:
  area.append(list(line[:-1]))

log_key = [[],[],[],[]]
history = [[],[],[],[]]

gap = 0
for q_cycle in range(4000000000):
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
  area = [[row[j] for row in area][::-1] for j in range(len(area[0]))]
  log_index = q_cycle%4
  area_str = ''.join(''.join(c for c in row) for row in area)
  if area_str in log_key[log_index]:
    gap = len(log_key[log_index]) - log_key[log_index].index(area_str)
    break
  log_key[log_index].append(area_str)
  # python lists screwed me here, need to copy each internal list per area
  # alternative is store the value instead of the array
  history[log_index].append([row[:] for row in area])

total = 0
for i, row in enumerate(history[3][(999999999 - q_cycle // 4) % gap + q_cycle // 4 - gap][::-1]):
  total += row.count('O') * (i+1)
print(total)

