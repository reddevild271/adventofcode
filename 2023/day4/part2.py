from sys import stdin

card_counts = [0]
current_card = 0

for line in stdin:
  card_counts[current_card] += 1
  
  win, player = line.split(':')[1].split('|')
  win = set([int(x) for x in win.split() if x])
  player = set([int(x) for x in player.split() if x])
  matches = len(win.intersection(player))
  while len(card_counts) < current_card + matches:
    card_counts.append(0)
  card_counts.append(0)
  for i in range(matches):
    card_counts[current_card + i + 1] += card_counts[current_card]
  
  current_card += 1

print(sum(card_counts))


