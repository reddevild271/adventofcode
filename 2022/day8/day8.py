from sys import stdin

# grid is square
grid = []
for line in stdin:
  grid.append([int(x) for x in line[:-1]])

visible = [[True for x in range(len(grid))]]
visible += [[True] + [False for x in range(len(grid)-2)] + [True] for x in range(len(grid)-2)]
visible += [[True for x in range(len(grid))]]

for i in range(1, len(grid)-1):
  max_top = grid[0][i]
  max_bot = grid[-1][i]
  max_left = grid[i][0]
  max_right = grid[i][-1]
  for j in range(1, len(grid)-1):
    if grid[j][i] > max_top:
      max_top = grid[j][i]
      visible[j][i] = True
    if grid[-j-1][i] > max_bot:
      max_bot = grid[-j-1][i]
      visible[-j-1][i] = True
    if grid[i][j] > max_left:
      max_left = grid[i][j]
      visible[i][j] = True
    if grid[i][-j-1] > max_right:
      max_right = grid[i][-j-1]
      visible[i][-j-1] = True

print(f'Part 1: {sum(row.count(True) for row in visible)}')

max_scenic = 0
for i in range(1, len(grid)-1):
  for j in range(1, len(grid)-1):
    top = 1
    y = i - 1
    while y > 0 and grid[y][j] < grid[i][j]:
      y -= 1
      top += 1
    bot = 1
    y = i + 1
    while y < len(grid) - 1 and grid[y][j] < grid[i][j]:
      y += 1
      bot += 1
    left = 1
    x = j - 1
    while x > 0 and grid[i][x] < grid[i][j]:
      x -= 1
      left += 1
    right = 1
    x = j + 1
    while x < len(grid) - 1 and grid[i][x] < grid[i][j]:
      x += 1
      right += 1
    scenic = top * bot * left * right
    if scenic > max_scenic:
      max_scenic = scenic

print(f'Part 2: {max_scenic}')
