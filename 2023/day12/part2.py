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
  a1 = arrange(springs, groups)
  a2 = arrange(springs+'?'+springs, groups*2)
  a3 = arrange(springs+'?'+springs+'?'+springs, groups*3)
  if a3 // a2 != a2 // a1:
    print(springs)
    print(groups)
    print(a1)
    print(a2)
    print(a3)
    print(arrange(((springs+'?')*4)[:-1], groups*4))
    print()
    total += arrange(((springs+'?')*5)[:-1], groups*5)
  else:
    total += a1 * (a2 // a1) ** 4
print(total)
