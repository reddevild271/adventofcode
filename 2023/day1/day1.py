from sys import stdin

total = 0
for line in stdin:
  first = False
  last_digit = 0
  for c in line:
    if c in '1234567890':
      if not first:
        total += int(c) * 10
        first = True
      last_digit = int(c)
  total += last_digit

print(total)
