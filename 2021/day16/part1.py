from sys import stdin

# type_id 4 (100) literal
def get_literal(s):
  idx = 0
  bits = s[1:5]
  while s[idx] == '1':
    idx += 5
    bits += s[idx+1:idx+5]
  return (int(bits,2),idx+5)

def packet_parser(s):
  version = int(s[:3],2)
  type_id = s[3:6]
  data = s[6:]
  if type_id == '100':
    return (version, 6+get_literal(data)[1])
  len_id = data[0]
  if len_id == '0':
    length = int(data[1:16],2)
    next_idx = 0
    while next_idx < length:
      result = packet_parser(data[16+next_idx:])
      version += result[0]
      next_idx += result[1]
    return (version, 22 + next_idx)
  num_sub = int(data[1:12],2)
  next_idx = 0
  for i in range(num_sub):
    result = packet_parser(data[12+next_idx:])
    version += result[0]
    next_idx += result[1]
  return (version, 18 + next_idx)
      
  
line = stdin.readline()[:-1]
b_str = bin(int(line, 16))[2:].zfill(len(line)*4)

print( packet_parser(b_str)[0] )


