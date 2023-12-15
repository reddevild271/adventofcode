from sys import stdin

def HASH(s):
  current_value = 0
  for c in s:
    current_value += ord(c)
    current_value *= 17
    current_value %= 256
  return current_value

print( sum(HASH(s) for s in stdin.read()[:-1].split(',')) )
