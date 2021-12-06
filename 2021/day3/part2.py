from sys import stdin

lines = stdin.read().splitlines()

def generate_rating( lines, step = 0, isO2 = True ):
  if len(lines) == 1:
    return lines[0][step:]
  zero = []
  one = []
  for line in lines:
    (zero if line[step] == '0' else one).append(line)
  tmp = len(zero) > len(one)
  if step == 0:
    return int(generate_rating( zero, 1, tmp ), 2) * int('1' + generate_rating( one, 1, not tmp ), 2)
  if isO2 == tmp:
    return '0' + generate_rating( zero, step + 1, isO2 )
  return '1' + generate_rating( one, step + 1, isO2 )

print( generate_rating( lines ) )
