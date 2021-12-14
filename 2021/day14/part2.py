from sys import stdin

template = stdin.readline()[:-1]

stdin.readline()

# rules dict
#
# key is element pair (rule)
# value is list of
# - output element for the rule
# - count of inputs to process per loop (starting with template)
# - count of total input processed (output)
rules = {}
for line in stdin:
  key, null, value = line.split()
  rules[key] = [value, template.count(key), 0]

for i in range(40):
  new_rules = {}
  for key, value in rules.items():
    key1 = key[0]+value[0]
    # add current rule input to key1 input
    if key1 in new_rules:
      new_rules[key1][1] += value[1]
    # if not in new_rules, maintain output value as well
    else:
      new_rules[key1] = [rules[key1][0], value[1], rules[key1][2]]
    key2 = value[0]+key[1]
    # add current rule input to key2 input
    if key2 in new_rules:
      new_rules[key2][1] += value[1]
    # if not in new_rules, maintain output value as well
    else:
      new_rules[key2] = [rules[key2][0], value[1], rules[key2][2]]
    # add current rule input to its new_rules output
    if key in new_rules:
      new_rules[key][2] += value[1]
    # if not in new_rules, maintain output value as well
    else:
      new_rules[key] = [value[0], 0, value[2]+value[1]]
  rules = new_rules

# count the elements in the original template
counts = {}
for c in template:
  if c in counts:
    counts[c] += 1
  else:
    counts[c] = 1

# add the counts of each rule's output element
for value in rules.values():
  if value[0] in counts:
    counts[value[0]] += value[2]
  else:
    counts[value[0]] = value[2]

print(max(counts.values()) - min(counts.values()))
