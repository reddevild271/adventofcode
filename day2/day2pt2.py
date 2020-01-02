# same as day 1 i just used guess and check in the input file
#
# I found you can treat the program as an ax + by + c equation
#
# x and y are the program inputs you change and with x = 0 and y = 0
# you get c = 1690717
#
# change x to 1 and you get 2590717, making a = 90000
#
# change y to 1 and you get 2590718, making b = 1
#
# the answer we are looking for is 19690720 so we subtract c, getting 18000003
#
# this translates to an x of 20 and a y of 3
#
# the answer is 100 * x + y so 100 * 20 + 3 which equals 2003

from sys import stdin

program = [int(x) for x in stdin.readline().split(',')]

i = 0
opcode = program[i]

while opcode in [1,2]:
  in1 = program[program[i+1]]
  in2 = program[program[i+2]]
  if opcode == 1:
    program[program[i+3]] = in1+in2
  else:
    program[program[i+3]] = in1*in2
  i += 4
  opcode = program[i]
    
print(program[0])
