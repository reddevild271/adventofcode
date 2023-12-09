from sys import stdin

def next(h):
  if len(set(h)) == 1:
    return h[0]
  h2 = []
  for i, v in enumerate(h[:-1]):
    h2.append(h[i+1] - v)
  return h[-1] + next(h2)

total = 0
for line in stdin:
  history = [int(x) for x in line.split()]
  total += next(history)
print(total)
  
