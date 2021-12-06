from sys import stdin

# input has 1000 lines of 12 bit numbers

one_bits = [0] * 12

for line in stdin:
  for i, c in enumerate(line):
    if c == '1':
      one_bits[i] += 1

gamma = ''
epsilon = ''

for one_cnt in one_bits:
  if one_cnt > 500:
    gamma += '1'
    epsilon += '0'
  else:
    gamma += '0'
    epsilon += '1'

print( int(gamma, 2) * int(epsilon, 2) )
