from sys import stdin

x = 1

during = [1]

for line in stdin:
  during.append(x)
  if line[0] != 'n':
    during.append(x)
    x += int(line[5:])

total = 0
for iss in [20,60,100,140,180,220]:
  total += during[iss] * iss
print(f'Part 1: {total}')

crt = ''
for row in range(6):
  for idx, pos in enumerate(during[40*row+1:40*(row+1)+1]):
    if idx in range(pos-1, pos+2):
      crt += '#'
    else:
      crt += '.'
  crt += '\n'

print(f'Part 2:\n{crt}')
