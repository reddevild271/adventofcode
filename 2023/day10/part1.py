from sys import stdin

class Pipe:
  N = None
  S = None
  E = None
  W = None

  x = 0
  y = 0

  c = ''

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
filler = [None]*len(pipe_grid[0])
pipe_grid = [filler] + pipe_grid + [filler]

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

steps = 0
last_pipe = None
path_pipe = start_pipe
while last_pipe is None or path_pipe != start_pipe:
  if path_pipe.N and path_pipe.N != last_pipe:
    last_pipe = path_pipe
    path_pipe = path_pipe.N
  elif path_pipe.S and path_pipe.S != last_pipe:
    last_pipe = path_pipe
    path_pipe = path_pipe.S
  elif path_pipe.W and path_pipe.W != last_pipe:
    last_pipe = path_pipe
    path_pipe = path_pipe.W
  elif path_pipe.E and path_pipe.E != last_pipe:
    last_pipe = path_pipe
    path_pipe = path_pipe.E
  steps += 1

print(steps // 2)
