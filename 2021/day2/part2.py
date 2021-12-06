from sys import stdin

x = 0
aim = 0
y = 0

for line in stdin:
  command, value = line.split()
  value = int(value)
  if command == 'forward':
    x += value
    y += aim * value
  elif command == 'down':
    aim += value
  elif command == 'up':
    aim -= value

print( x * y )
