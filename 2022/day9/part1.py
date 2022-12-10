from sys import stdin

hx = 0
hy = 0
tx = 0
ty = 0

xdif_dict = { 'U': 0, 'L': -1, 'R': 1, 'D':  0 }
ydif_dict = { 'U': 1, 'L':  0, 'R': 0, 'D': -1 }

tail_seen = { (0,0) }

for line in stdin:
  line = line.split()
  udlr = line[0]
  xdif = xdif_dict[udlr]
  ydif = ydif_dict[udlr]
  for i in range(int(line[1])):
    if abs(hx + xdif - tx) > 1 or abs(hy + ydif - ty) > 1:
      tx = hx
      ty = hy
      tail_seen.add((tx,ty))
    hx += xdif
    hy += ydif

print(len(tail_seen))
