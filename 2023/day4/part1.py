from sys import stdin

total = 0
for line in stdin:
  win, player = line.split(':')[1].split('|')
  win = set([int(x) for x in win.split() if x])
  player = set([int(x) for x in player.split() if x])
  matches = len(win.intersection(player))
  if matches > 0:
    total += 2 ** (matches - 1)

print(total)


