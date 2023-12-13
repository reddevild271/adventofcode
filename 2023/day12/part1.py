from sys import stdin

def arrange(s, g):
  min_len_g = sum(g) + len(g) - 1
  if min_len_g < 0:
    return 1 if '#' not in s else 0
  total = 0
  i = 0
  while i + min_len_g <= len(s):
    if all(c in '?#' for c in s[i:i+g[0]]) and (i+g[0] == len(s) or s[i+g[0]] in '.?'):
      total += arrange(s[i+g[0]+1:], g[1:])
    if s[i] == '#':
      return total
    i += 1
  return total

total = 0
for line in stdin:
  springs, groups = line.split()
  groups = [int(x) for x in groups.split(',')]
  total += arrange(springs, groups)
print(total)
