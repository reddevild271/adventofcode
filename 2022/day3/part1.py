from sys import stdin

priorities = 0
for line in stdin:
  item_cnt = len(line)//2
  wrong_item = ord(list(set(line[:item_cnt]).intersection(line[item_cnt:-1]))[0])
  if wrong_item > 96:
    priorities += wrong_item - 96
  else:
    priorities += wrong_item - 38

print(priorities)
