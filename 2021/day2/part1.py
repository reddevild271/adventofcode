from sys import stdin

x = 0
y = 0

for line in stdin:
  command, value = line.split()
  value = int(value)
  if command == 'forward':
    x += value
  elif command == 'down':
    y += value
  elif command == 'up':
    y -= value

print( x * y )
