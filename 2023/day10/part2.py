from sys import stdin

class Pipe:
  N = None
  S = None
  E = None
  W = None

  x = 0
  y = 0

  c = ''

  def __str__(self):
    return self.c

  def __repr__(self):
    return self.c

# parse input
pipe_grid = []
start_pipe = None

y = 0
for line in stdin:
  row = []
  for x, c in enumerate(line[:-1]):
    if c == '.':
      row.append(None)
      continue
    pipe = Pipe()
    pipe.x = x + 1
    pipe.y = y + 1
    pipe.c = c
    if c == 'S':
      start_pipe = pipe
    row.append(pipe)
  pipe_grid.append([None] + row + [None])
  y += 1

# create border around input
filler = [None]*len(pipe_grid[0])
pipe_grid = [filler] + pipe_grid + [filler]

# attach pipes to each other
for row in pipe_grid:
  for pipe in row:
    if pipe is None:
      continue
    pipe_N = pipe_grid[pipe.y - 1][pipe.x]
    pipe_S = pipe_grid[pipe.y + 1][pipe.x]
    pipe_W = pipe_grid[pipe.y][pipe.x - 1]
    pipe_E = pipe_grid[pipe.y][pipe.x + 1]
    #|-LJ7FS
    if pipe.c in '|LJS' and pipe_N and pipe_N.c in '|7FS':
      pipe.N = pipe_N
      pipe_N.S = pipe
    if pipe.c in '|7FS' and pipe_S and pipe_S.c in '|LJS':
      pipe.S = pipe_S
      pipe_S.N = pipe
    if pipe.c in '-J7S' and pipe_W and pipe_W.c in '-LFS':
      pipe.W = pipe_W
      pipe_W.E = pipe
    if pipe.c in '-LFS' and pipe_E and pipe_E.c in '-J7S':
      pipe.E = pipe_E
      pipe_E.W = pipe

# generate the main pipe loop and determine whether it turns right or left
last_pipe = None
path_pipe = start_pipe
path_loop = []
last_dir = None
turns = 0 # right positive
while last_pipe is None or path_pipe != start_pipe:
  path_loop.append(path_pipe)
  if path_pipe.N and path_pipe.N != last_pipe:
    last_pipe = path_pipe
    path_pipe = path_pipe.N
    if path_pipe.W:
      turns -= 1
    elif path_pipe.E:
      turns += 1
  elif path_pipe.S and path_pipe.S != last_pipe:
    last_pipe = path_pipe
    path_pipe = path_pipe.S
    if path_pipe.W:
      turns += 1
    elif path_pipe.E:
      turns -= 1
  elif path_pipe.W and path_pipe.W != last_pipe:
    last_pipe = path_pipe
    path_pipe = path_pipe.W
    if path_pipe.N:
      turns += 1
    elif path_pipe.S:
      turns -= 1
  elif path_pipe.E and path_pipe.E != last_pipe:
    last_pipe = path_pipe
    path_pipe = path_pipe.E
    if path_pipe.N:
      turns -= 1
    elif path_pipe.S:
      turns += 1

# remove pipes out of the main loop
for y in range(len(pipe_grid)):
  for x in range(len(pipe_grid[y])):
    if pipe_grid[y][x] not in path_loop:
      pipe_grid[y][x] = None

area_count = 0

# traverse the x or y direction until a pipe is hit
# modifies grid in place to keep track of newfound spaces
# returns count of newfound spaces hit
def find_space(grid, y, y_inc, x, x_inc):
  count = 0
  y += y_inc
  x += x_inc
  while grid[y][x] is True or grid[y][x] is None:
    if grid[y][x] is None:
      count += 1
    grid[y][x] = True
    x += x_inc
    y += y_inc
  return count

# search the right or left side of each pipe in the main loop for empty space
for pipe1, pipe2 in zip(path_loop[:-1], path_loop[1:]):
  # if pipe 1 goes North into pipe 2
  if pipe2 is pipe1.N:
    # if main loop turns right
    if turns > 0:
      # find new spaces from pipe 1 to the right ( pipe is going North, so East )
      area_count += find_space(pipe_grid, pipe1.y, 0, pipe1.x, 1)
      # if pipe 1 is a left hand turn ( came from West, goes to North )
      if pipe1.W:
        # find new spaces in the oppposite direction of the turn ( South )
        area_count += find_space(pipe_grid, pipe1.y, 1, pipe1.x, 0)
    # if main loop turns left
    else:
      # find new spaces from pipe 1 to the left ( pipe is going North, so West )
      area_count += find_space(pipe_grid, pipe1.y, 0, pipe1.x, -1)
      # if pipe 1 is a right hand turn ( came from East, goes to North )
      if pipe1.E:
        # find new spaces in the oppposite direction of the turn ( South )
        area_count += find_space(pipe_grid, pipe1.y, 1, pipe1.x, 0)
  if pipe2 is pipe1.S:
    if turns > 0:
      area_count += find_space(pipe_grid, pipe1.y, 0, pipe1.x, -1)
      if pipe1.E:
        area_count += find_space(pipe_grid, pipe1.y, -1, pipe1.x, 0)
    else:
      area_count += find_space(pipe_grid, pipe1.y, 0, pipe1.x, 1)
      if pipe1.W:
        area_count += find_space(pipe_grid, pipe1.y, -1, pipe1.x, 0)
  if pipe2 is pipe1.W:
    if turns > 0:
      area_count += find_space(pipe_grid, pipe1.y, -1, pipe1.x, 0)
      if pipe1.S:
        area_count += find_space(pipe_grid, pipe1.y, 0, pipe1.x, 1)
    else:
      area_count += find_space(pipe_grid, pipe1.y, 1, pipe1.x, 0)
      if pipe1.N:
        area_count += find_space(pipe_grid, pipe1.y, 0, pipe1.x, 1)
  if pipe2 is pipe1.E:
    if turns > 0:
      area_count += find_space(pipe_grid, pipe1.y, 1, pipe1.x, 0)
      if pipe1.N:
        area_count += find_space(pipe_grid, pipe1.y, 0, pipe1.x, -1)
    else:
      area_count += find_space(pipe_grid, pipe1.y, -1, pipe1.x, 0)
      if pipe1.S:
        area_count += find_space(pipe_grid, pipe1.y, 0, pipe1.x, -1)
          
#### print grid
##for row in pipe_grid:
##  s = ''
##  for n in row:
##    if n is True:
##      s += 'T'
##    elif n in path_loop:
##      s += str(n)
##    else:
##      s += ' '
##  print(s)

print(area_count)
