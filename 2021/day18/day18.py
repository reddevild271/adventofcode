from sys import stdin
from copy import deepcopy

def explode(num, depth=0):
  if depth == 4:
    return []
  indices = [[],[]]
  for i in range(2):
    if type(num[i]) == list:
      indices[i] = [i] + explode(num[i], depth+1)
      if len(indices[i]) == 4:
        num_tmp = num
        last_left = None
        last_right = None
        last_parent = None
        for idx, j in enumerate(indices[i]):
          if j == 0:
            last_left = num_tmp
          else:
            last_right = num_tmp
          last_parent = num_tmp
          num_tmp = num_tmp[j]
        left, right = num_tmp
        last_parent[indices[i][-1]] = 0
        if last_right != None:
          if type(last_right[0]) == list:
            last_right = last_right[0]
            while type(last_right[1]) == list:
              last_right = last_right[1]
            last_right[1] += left
          else:
            last_right[0] += left
        if last_left != None:
          if type(last_left[1]) == list:
            last_left = last_left[1]
            while type(last_left[0]) == list:
              last_left = last_left[0]
            last_left[0] += right
          else:
            last_left[1] += right
        return True
      elif len(indices[i]) + depth == 4:
        return indices[i]
  return []

def split(num):
  for i in range(2):
    if type(num[i]) == list:
      if split(num[i]):
        return True
    elif num[i] >= 10:
      div2 = num[i] // 2
      num[i] = [div2, num[i] - div2]
      return True
  return False

def reduce(num):
  while explode(num) is True:
    continue
  if split(num):
    reduce(num)

def magnitude(num):
  if type(num) == list:
    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])
  return num

nums = [eval(line) for line in stdin]

num_sum = deepcopy(nums[0])
for num in nums[1:]:
  num_sum = [num_sum, deepcopy(num)]
  reduce(num_sum)

print('Part 1: ' + str(magnitude(num_sum)))

max_mag = 0
for num1 in nums:
  for num2 in nums:
    if num1 == num2:
      continue
    num_sum = [deepcopy(num1), deepcopy(num2)]
    reduce(num_sum)
    max_mag = max(max_mag, magnitude(num_sum))

print('Part 2: ' + str(max_mag))
