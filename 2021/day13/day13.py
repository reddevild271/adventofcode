from sys import stdin

paper = set()
fold_dir = []
fold_idx = []

fold_mode = False
for line in stdin:
  if line == '\n':
    fold_mode = True
  elif fold_mode:
    d, idx = line.split()[-1].split('=')
    fold_dir.append(d)
    fold_idx.append(int(idx))
  else:
    paper.add(tuple([int(x) for x in line[:-1].split(',')]))

for i in range(len(fold_dir)):
  d = fold_dir[i]
  idx = fold_idx[i]
  new_paper = set()
  if d == 'x':
    for pt in paper:
      if pt[0] > idx:
        new_paper.add((2*idx-pt[0],pt[1]))
      elif pt[0] < idx:
        new_paper.add(pt)
  if d == 'y':
    for pt in paper:
      if pt[1] > idx:
        new_paper.add((pt[0],2*idx-pt[1]))
      elif pt[1] < idx:
        new_paper.add(pt)
  paper = new_paper
  if i == 0:
    print("Part 1: " + str(len(paper)))
    print()

print("Part 2:")
for i in range(6):
  for j in range(39):
    if (j,i) in paper:
      print("#",end='')
    else:
      print(" ",end='')
  print()
