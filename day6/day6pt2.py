from sys import stdin

orbit_map = {}

for line in stdin:
  y, x = line[:-1].split(')')
  orbit_map[x] = y

you_map = []
you = 'YOU'
while you != 'COM':
  you = orbit_map[you]
  you_map += [you]

i = 0
san = 'SAN'
while san not in you_map:
  i += 1
  san = orbit_map[san]

print(i+you_map.index(san)-1)
