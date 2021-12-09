from sys import stdin    

def basin_size(row,col,system,checked):
  if (row,col) in checked:
    return 0
  checked.add((row,col))
  if system[row][col] == 9:
    return 0
  return 1 + basin_size(row-1,col,system,checked) \
           + basin_size(row,col-1,system,checked) \
           + basin_size(row+1,col,system,checked) \
           + basin_size(row,col+1,system,checked) \

system = [[9]+[int(c) for c in line[:-1]]+[9] for line in stdin]
system = [[9]*(len(system[0]))] + system + [[9]*(len(system[0]))]

basins = []
checked = set()

for row in range(1,len(system)-1):
  for col in range(1,len(system[0])-1):
    basins.append(basin_size(row,col,system,checked))

top_basins = sorted(basins)[-3:]
print(top_basins[0]*top_basins[1]*top_basins[2])
