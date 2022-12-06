from sys import stdin

outcomes = {'A': {'X': 3, 'Y': 4, 'Z': 8 },
            'B': {'X': 1, 'Y': 5, 'Z': 9 },
            'C': {'X': 2, 'Y': 6, 'Z': 7 }}

# B X 1
# C X 2
# A X 3 Y 4
# B     Y 5
# C     Y 6 Z 7
# A         Z 8
# B         Z 9
# 
# us = ord(line[2]) - ord('X')
# X = 0
# Y = 1
# Z = 2
# 
# start = us * 3 + 1
# X start = 1
# Y start = 4
# Z start = 7
# 
# them = ord(line[0]) - ord('A')
# A = 0
# B = 1
# C = 2
# 
# us_them = us - 1
# X_them = -1
# Y_them = 0
# Z_them = 1
# 
# addition = start + ( them + us_them ) % 3

score_lookup = 0
score_math = 0
for line in stdin:
  score_lookup += outcomes[line[0]][line[2]]

  us = ord(line[2]) - ord('X')
  them = ord(line[0]) - ord('A')
  score_math += us * 3 + 1 + ( them + us - 1 ) % 3
  
  
print(f"Part 2 (lookup): {score_lookup}")
print(f"Part 2   (math): {score_math}")
