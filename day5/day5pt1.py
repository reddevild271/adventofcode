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
pgmInput = [1]
pic = 0
pgmOutput = []
paramFuncs = {0:(lambda x: program[x]),
              1:(lambda x: x)}

i = 0
opcode = Opcode(program[i])

while True:
  if opcode.code == 1:
    in1 = program[paramFuncs[opcode.params[0]](i+1)]
    in2 = program[paramFuncs[opcode.params[1]](i+2)]
    program[paramFuncs[opcode.params[2]](i+3)] = in1+in2
    i += 4
  elif opcode.code == 2:
    in1 = program[paramFuncs[opcode.params[0]](i+1)]
    in2 = program[paramFuncs[opcode.params[1]](i+2)]
    program[paramFuncs[opcode.params[2]](i+3)] = in1*in2
    i += 4
  elif opcode.code == 3:
    program[paramFuncs[opcode.params[0]](i+1)] = pgmInput[pic]
    pic += 1
    i += 2
  elif opcode.code == 4:
    pgmOutput += [program[paramFuncs[opcode.params[0]](i+1)]]
    i += 2
  else:
    break
  opcode = Opcode(program[i])
    
print(pgmOutput)
