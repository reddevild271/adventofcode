from sys import stdin

galaxies = []

y = 0
for line in stdin:
  no_galaxy = True
  for i, c in enumerate(line[:-1]):
    if c == '#':
      galaxies.append([i,y])
      no_galaxy = False
  if no_galaxy:
    y += 1
  y += 1

x_locations = sorted(set(g[0] for g in galaxies))
x_empty = [x for x in range(x_locations[0] + 1, x_locations[-1]) if x not in x_locations]

for g in galaxies:
  x_inc = 0
  for x_e in x_empty:
    if g[0] > x_e:
      x_inc += 1
    else:
      break
  g[0] += x_inc

total = 0
for i, g1 in enumerate(galaxies):
  for g2 in galaxies[i+1:]:
    total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
print(total)
