from sys import stdin

def flash(octopi, row, col):
  if row not in range(len(octopi)) or \
     col not in range(len(octopi[row])):
    return 0
  octopi[row][col] += 1
  if octopi[row][col] == 10:
    return flash(octopi, row-1, col-1) + \
           flash(octopi, row-1, col)   + \
           flash(octopi, row-1, col+1) + \
           flash(octopi, row, col-1)   + \
           flash(octopi, row, col+1)   + \
           flash(octopi, row+1, col-1) + \
           flash(octopi, row+1, col)   + \
           flash(octopi, row+1, col+1) + 1
  return 0

octopi = [[int(c) for c in line[:-1]] for line in stdin]

flashes = 0
for i in range(100):
  for row in range(len(octopi)):
    for col in range(len(octopi[row])):
      flashes += flash(octopi, row, col)
  for row in range(len(octopi)):
    for col in range(len(octopi[row])):
      if octopi[row][col] > 9:
        octopi[row][col] = 0

print(flashes)
