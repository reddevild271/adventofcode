from sys import stdin

search_strs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
search_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

total = 0
for line in stdin:
  first = [line.find(s) for s in search_strs]
  first_max = max(first) + 1
  first = [x if x >= 0 else first_max for x in first]
  total += 10 * search_nums[first.index(min(first))]
  
  last = [line.rfind(s) for s in search_strs]
  total += search_nums[last.index(max(last))]

print(total)
