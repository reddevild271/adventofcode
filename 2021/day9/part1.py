from sys import stdin    

system = [[10]+[int(c) for c in line[:-1]]+[10] for line in stdin]
system = [[10]*(len(system[0]))] + system + [[10]*(len(system[0]))]

risk_level = 0
for row in range(1,len(system)-1):
  for col in range(1,len(system[0])-1):
    if system[row][col] < min([system[row-1][col],
                               system[row][col-1],
                               system[row+1][col],
                               system[row][col+1]]):
      risk_level += system[row][col]+1
print(risk_level)
