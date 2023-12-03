from sys import stdin

class Label:
  row = 0
  col_start = 0
  col_end = 0
  int_value = 0

class Gear:
  row = 0
  col = 0

labels = []
gears = []

row = 0
for line in stdin:
  label_start = 0
  num_str = ''
  for col, c in enumerate(line):
    if c in '0123456789':
      if not num_str:
        label_start = col
      num_str += c
      continue
    if num_str:
      label = Label()
      label.row = row
      label.col_start = label_start
      label.col_end = col - 1
      label.int_value = int(num_str)
      labels.append(label)
      num_str = ''
    if c == '*':
      gear = Gear()
      gear.row = row
      gear.col = col
      gears.append(gear)
  row += 1

total = 0

for gear in gears:
  ratios = []
  for label in labels:
    if label.row not in [gear.row - 1, gear.row, gear.row + 1]:
      continue
    if gear.col not in range(label.col_start - 1, label.col_end + 2):
      continue
    ratios.append(label.int_value)
  if len(ratios) == 2:
    total += ratios[0] * ratios[1]

print(total)

