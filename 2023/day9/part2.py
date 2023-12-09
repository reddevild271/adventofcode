from sys import stdin

def prev(h, even):
  if len(set(h)) == 1:
    return h[0] if even else -h[0]
  h2 = []
  for i, v in enumerate(h[:-1]):
    h2.append(h[i+1] - v)
  return (h[0] if even else -h[0]) + prev(h2, not even)

total = 0
for line in stdin:
  history = [int(x) for x in line.split()]
  total += prev(history, True)
print(total)
