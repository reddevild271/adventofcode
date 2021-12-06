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
