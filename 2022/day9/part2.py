from sys import stdin

knots = 10
kx = [0 for i in range(knots)]
ky = [0 for i in range(knots)]
kseen = [{(0,0)} for i in range(knots)]

# switched sign of up/down from part 1 for easier lookup table
xdif_dict = { 'U':  0, 'L': -1, 'R': 1, 'D': 0 }
ydif_dict = { 'U': -1, 'L':  0, 'R': 0, 'D': 1 }

x_lookup = [[-1, -1, 0, 1, 1],
            [-1,  0, 0, 0, 1],
            [-1,  0, 0, 0, 1],
            [-1,  0, 0, 0, 1],
            [-1, -1, 0, 1, 1]]

y_lookup = [[-1, -1, -1, -1, -1],
            [-1,  0,  0,  0, -1],
            [ 0,  0,  0,  0,  0],
            [ 1,  0,  0,  0,  1],
            [ 1,  1,  1,  1,  1]]

for line in stdin:
  line = line.split()
  udlr = line[0]
  for i in range(int(line[1])):
    kx[0] += xdif_dict[udlr]
    ky[0] += ydif_dict[udlr]
    kseen[0].add((kx[0],ky[0]))
    for k in range(1,knots):
      xdif = kx[k-1] - kx[k] + 2
      ydif = ky[k-1] - ky[k] + 2
      kx[k] += x_lookup[ydif][xdif]
      ky[k] += y_lookup[ydif][xdif]
      kseen[k].add((kx[k],ky[k]))

print(len(kseen[9]))
