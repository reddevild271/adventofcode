from sys import stdin
from collections import Counter

template = stdin.readline()[:-1]

stdin.readline()

rules = {}
for line in stdin:
  key, null, value = line.split()
  rules[key] = value

for x in range(10):
  new_template = ''
  for i in range(len(template)-1):
    new_template += template[i] + rules[template[i:i+2]]
  template = new_template + template[-1]

template_counter = Counter(template)
commonality = template_counter.most_common()
print( commonality[0][1] - commonality[-1][1] )
