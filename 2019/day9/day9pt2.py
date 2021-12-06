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

program = [int(x) for x in stdin.readline().split(',')] + [0]*10000
pgmInput = [2]
pic = 0
pgmOutput = []
relBase = 0

i = 0
opcode = Opcode(program[i])

paramFuncs = {0:(lambda x: program[x]),
              1:(lambda x: x),
              2:(lambda x: relBase+program[x])}

bambdaRead = lambda x: program[bambdaWrite(x)]
bambdaWrite = lambda x: paramFuncs[opcode.params[x-1]](i+x)

while True:
  if opcode.code == 1:
    in1 = bambdaRead(1)
    in2 = bambdaRead(2)
    program[bambdaWrite(3)] = in1+in2
    i += 4
  elif opcode.code == 2:
    in1 = bambdaRead(1)
    in2 = bambdaRead(2)
    program[bambdaWrite(3)] = in1*in2
    i += 4
  elif opcode.code == 3:
    program[bambdaWrite(1)] = pgmInput[pic]
    pic += 1
    i += 2
  elif opcode.code == 4:
    pgmOutput += [bambdaRead(1)]
    i += 2
  elif opcode.code == 5:
    if bambdaRead(1):
      i = bambdaRead(2)
    else:
      i += 3
  elif opcode.code == 6:
    if not bambdaRead(1):
      i = bambdaRead(2)
    else:
      i += 3
  elif opcode.code == 7:
    program[bambdaWrite(3)] = int(bambdaRead(1) < bambdaRead(2))
    i += 4
  elif opcode.code == 8:
    program[bambdaWrite(3)] = int(bambdaRead(1) == bambdaRead(2))
    i += 4
  elif opcode.code == 9:
    relBase += bambdaRead(1)
    i += 2
  else:
    break
  opcode = Opcode(program[i])
    
print(pgmOutput)
