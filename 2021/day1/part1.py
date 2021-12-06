from sys import stdin

last_depth = int(stdin.readline())
inc_cnt = 0

for line in stdin:
  depth = int(line)
  if depth > last_depth:
    inc_cnt += 1
  last_depth = depth

print(inc_cnt)
