from sys import stdin

count = 0
for line in stdin:
  test, output = line.split('|')
  for s in output.split():
    if len(s) in [2,3,4,7]:
      count += 1

print(count)
