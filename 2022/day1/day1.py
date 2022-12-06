from sys import stdin

food_list = []
food = 0
for line in stdin:
  if line == '\n':
    food_list.append( food )
    food = 0
  else:
    food += int(line)
food_list.sort()
print(f"Part 1: {food_list[-1]}")
print(f"Part 2: {sum(food_list[-3:])}")
