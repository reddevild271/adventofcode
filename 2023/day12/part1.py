from sys import stdin

def arrange(s, g):
  test1 = len(g) == 0
  test2 = set(s).issubset('. ?')
  if test1:
    if test2:
      return 1
    return 0
  elif test2:
    return 0
    
  total = 0
  min_len_g = sum(g) + len(g) - 1
  i = 0
  while i < len(s) - min_len_g:
    if all(c in '?#' for c in s[i:i+g[0]]) and s[i+g[0]] in '.? ':
      total += arrange(s[i+g[0]+1:], g[1:])
    while s[i] == '#':
      i += 1
    else:
      i += 1
  return total

total = 0
for line in stdin:
  springs, groups = line.split()
  groups = [int(x) for x in groups.split(',')]
  total += arrange(springs+' ', groups)
print(total)
