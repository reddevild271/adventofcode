from sys import stdin

depth1 = int(stdin.readline())
depth2 = int(stdin.readline())
depth3 = int(stdin.readline())

last_sum = depth1 + depth2 + depth3

inc_cnt = 0

for line in stdin:
  depth1 = depth2
  depth2 = depth3
  depth3 = int(line)
  new_sum = depth1 + depth2 + depth3
  if new_sum > last_sum:
    inc_cnt += 1
  last_sum = new_sum

print(inc_cnt)
