from sys import stdin

class Label:
  row = 0
  col_start = 0
  col_end = 0
  int_value = 0

class Symbol:
  row = 0
  col = 0

labels = []
symbols = []

parts = 0

row = 0
for line in stdin:
  label_start = 0
  num_str = ''
  special = False
  for col, c in enumerate(line):
    if c in '0123456789':
      if not num_str:
        label_start = col
      num_str += c
    elif c in '.\n':
      if num_str:
        if special:
          parts += int(num_str)
        else:
          label = Label()
          label.row = row
          label.col_start = label_start
          label.col_end = col - 1
          label.int_value = int(num_str)
          labels.append(label)
        num_str = ''
      special = False
    else:
      if num_str:
        parts += int(num_str)
        num_str = ''
      symbol = Symbol()
      symbol.row = row
      symbol.col = col
      symbols.append(symbol)
      special = True
  row += 1

for label in labels:
  for symbol in symbols:
    if label.row not in [symbol.row - 1, symbol.row, symbol.row + 1]:
      continue
    if symbol.col not in range(label.col_start - 1, label.col_end + 2):
      continue
    parts += label.int_value
    break

print(parts)

