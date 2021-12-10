from sys import stdin

chunk_start = {')':'(',
               ']':'[',
               '}':'{',
               '>':'<'}

chunk_score = {')':3,
               ']':57,
               '}':1197,
               '>':25137}

score = 0
for line in stdin:
  stack = []
  for c in line:
    if c in [')',']','}','>']:
      if stack[-1] != chunk_start[c]:
        score += chunk_score[c]
        break
      stack.pop()
    else:
      stack.append(c)

print(score)
