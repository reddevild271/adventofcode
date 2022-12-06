from sys import stdin

outcomes = {'A': {'X': 4, 'Y': 8, 'Z': 3 },
            'B': {'X': 1, 'Y': 5, 'Z': 9 },
            'C': {'X': 7, 'Y': 2, 'Z': 6 }}

score_lookup = 0
score_math = 0
for line in stdin:
  score_lookup += outcomes[line[0]][line[2]]
  score_math += (3 * (ord('B') - ord(line[0])) + 4 * (ord(line[2]) - ord('X'))) % 9 + 1

print(f"Part 1 (lookup): {score_lookup}")
print(f"Part 1   (math): {score_math}")
