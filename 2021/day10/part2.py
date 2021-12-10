from sys import stdin

chunk_start = {')':'(',
               ']':'[',
               '}':'{',
               '>':'<'}

chunk_score = {'(':1,
               '[':2,
               '{':3,
               '<':4}

incomplete = []

scores = []
for line in stdin:
  stack = []
  corrupt = False
  score = 0
  for c in line[:-1]:
    if c in [')',']','}','>']:
      if stack[-1] != chunk_start[c]:
        corrupt = True
        break
      stack.pop()
    else:
      stack.append(c)
  if not corrupt:
    while len(stack) > 0:
      score = score * 5 + chunk_score[stack.pop()]
    scores.append(score)

print(sorted(scores)[len(scores)//2])
