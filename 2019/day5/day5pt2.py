from sys import stdin

class Opcode:
  def __init__(self, opcode):
    soc = str(opcode)
    if len(soc) > 2:
      self.code = int(soc[-2:])
      self.params = [int(x) for x in soc[-3::-1]] + [0,0]
    else:
      self.code = opcode
      self.params = [0,0,0]

program = [int(x) for x in stdin.readline().split(',')]
pgmInput = [5]
pic = 0
pgmOutput = []

i = 0
opcode = Opcode(program[i])

paramFuncs = {0:(lambda x: program[program[x]]),
              1:(lambda x: program[x])}

bambda = lambda x: paramFuncs[opcode.params[x-1]](i+x)

while True:
  if opcode.code == 1:
    in1 = bambda(1)
    in2 = bambda(2)
    program[program[i+3]] = in1+in2
    i += 4
  elif opcode.code == 2:
    in1 = bambda(1)
    in2 = bambda(2)
    program[program[i+3]] = in1*in2
    i += 4
  elif opcode.code == 3:
    program[program[i+1]] = pgmInput[pic]
    pic += 1
    i += 2
  elif opcode.code == 4:
    pgmOutput += [bambda(1)]
    i += 2
  elif opcode.code == 5:
    if bambda(1):
      i = bambda(2)
    else:
      i += 3
  elif opcode.code == 6:
    if not bambda(1):
      i = bambda(2)
    else:
      i += 3
  elif opcode.code == 7:
    program[program[i+3]] = int(bambda(1) < bambda(2))
    i += 4
  elif opcode.code == 8:
    program[program[i+3]] = int(bambda(1) == bambda(2))
    i += 4
  else:
    break
  opcode = Opcode(program[i])
    
print(pgmOutput)
