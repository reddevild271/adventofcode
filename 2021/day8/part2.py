from sys import stdin
from time import sleep

segments = {0:set([0,1,2,4,5,6]),
            1:set([2,5]),
            2:set([0,2,3,4,6]),
            3:set([0,2,3,5,6]),
            4:set([1,2,3,5]),
            5:set([0,1,3,5,6]),
            6:set([0,1,3,4,5,6]),
            7:set([0,2,5]),
            8:set([0,1,2,3,4,5,6]),
            9:set([0,1,2,3,5,6])}

length_to_segs = {2:set([2,5]),
                  3:set([0,2,5]),
                  4:set([1,2,3,5])}

count = 0
for line in stdin:
  line = line.replace('| ','')
  tests = line.split()
  test_map = {'a':set([0,1,2,3,4,5,6]),
              'b':set([0,1,2,3,4,5,6]),
              'c':set([0,1,2,3,4,5,6]),
              'd':set([0,1,2,3,4,5,6]),
              'e':set([0,1,2,3,4,5,6]),
              'f':set([0,1,2,3,4,5,6]),
              'g':set([0,1,2,3,4,5,6])}
  for test in tests:
    if len(test) in length_to_segs:
      for t in test:
        test_map[t] &= length_to_segs[len(test)]

  while max([len(x) for x in test_map.values()]) > 2:
    for key, value in test_map.items():
      same_keys = []
      for key2, value2 in test_map.items():
        if value == value2:
          same_keys.append(key2)
      if len(value) == len(same_keys):
        for key2, value2 in test_map.items():
          if key2 not in same_keys:
            value2 -= value

  test_maps = [{} for i in range(8)]
  first13 = True
  first25 = True
  first46 = True
  for key, value in test_map.items():
    if value == set([1,3]):
      if first13:
        for i in range(8):
          if i%2 == 0:
            test_maps[i][key] = 1
          else:
            test_maps[i][key] = 3
        first13 = False
      else:
        for i in range(8):
          if i%2 == 0:
            test_maps[i][key] = 3
          else:
            test_maps[i][key] = 1
    elif value == set([2,5]):
      if first25:
        for i in range(8):
          if i//2%2 == 0:
            test_maps[i][key] = 2
          else:
            test_maps[i][key] = 5
        first25 = False
      else:
        for i in range(8):
          if i//2%2 == 0:
            test_maps[i][key] = 5
          else:
            test_maps[i][key] = 2
    elif value == set([4,6]):
      if first46:
        for i in range(8):
          if i//4%2 == 0:
            test_maps[i][key] = 4
          else:
            test_maps[i][key] = 6
        first46 = False
      else:
        for i in range(8):
          if i//4%2 == 0:
            test_maps[i][key] = 6
          else:
            test_maps[i][key] = 4
    else:
      for i in range(8):
        test_maps[i][key] = 0

  for tm in test_maps:
    bad_tm = False
    digits = []
    for test in tests:
      test_set = set()
      for t in test:
        test_set.add(tm[t])
      if test_set not in segments.values():
        bad_tm = True
        break
      for key, value in segments.items():
        if value == test_set:
          digits.append(key)
    if not bad_tm:
      count += int(''.join([str(x) for x in digits[-4:]]))

print(count)
