from sys import stdin

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
  type_id = int(s[3:6],2)
  if type_id == 4:
    idx = 6
    bits = s[idx+1:idx+5]
    while s[idx] == '1':
      idx += 5
      bits += s[idx+1:idx+5]
    return (int(bits,2), idx+5)
  len_id = s[6]
  idx = 0
  items = []
  if len_id == '0':
    length = int(s[7:22],2)
    while idx < length:
      result = packet_parser(s[idx+22:])
      items.append(result[0])
      idx += result[1]
    return (operate(type_id, items), idx+22)
  num_sub = int(s[7:18],2)
  for i in range(num_sub):
    result = packet_parser(s[idx+18:])
    items.append(result[0])
    idx += result[1]
  return (operate(type_id, items), idx+18)
      
  
line = stdin.readline()[:-1]
b_str = bin(int(line, 16))[2:].zfill(len(line)*4)

print( packet_parser(b_str)[0] )


