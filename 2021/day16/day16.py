from sys import stdin

def iterate(len_id, s, idx, i):
  if len_id == '0':
    return idx < int(s[7:22],2)+22
  return i < int(s[7:18],2)

def operate(type_id, items):
  if type_id == 0:
    return sum(items)
  if type_id == 1:
    x = 1
    for i in items:
      x *= i
    return x
  if type_id == 2:
    return min(items)
  if type_id == 3:
    return max(items)
  if type_id == 5:
    return 1 if items[0] > items[1] else 0
  if type_id == 6:
    return 1 if items[0] < items[1] else 0
  if type_id == 7:
    return 1 if items[0] == items[1] else 0

def packet_parser(s):
  version = int(s[:3],2)
  type_id = int(s[3:6],2)
  if type_id == 4:
    idx = 6
    bits = s[idx+1:idx+5]
    while s[idx] == '1':
      idx += 5
      bits += s[idx+1:idx+5]
    return version, [int(bits,2)], idx+5
  len_id = s[6]
  i = 0
  result = [version, [], 22 if len_id == '0' else 18]
  while iterate(len_id, s, result[2], i):
    result = [x+y for x, y in zip(result, packet_parser(s[result[2]:]))]
    i += 1
  return result[0], [operate(type_id, result[1])], result[2]

line = stdin.readline()[:-1]
b_str = bin(int(line, 16))[2:].zfill(len(line)*4)
result = packet_parser(b_str)
print( 'Part 1: ' + str(result[0]) )
print( 'Part 2: ' + str(result[1][0]) )
