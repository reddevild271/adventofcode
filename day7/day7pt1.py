from sys import stdin
from itertools import permutations

class Opcode:
  def __init__(self, opcode):
    soc = str(opcode)
    if len(soc) > 2:
      self.code = int(soc[-2:])
      self.params = [int(x) for x in soc[-3::-1]] + [0,0]
    else:
      self.code = opcode
      self.params = [0,0,0]

class Amp:
  def __init__(self, phase, signal, program):
    self.program = program[:]
    self.pic = 0
    self.pgmInput = [phase,signal]
    self.pgmOutput = []
    self.i = 0
    self.opcode = Opcode(program[self.i])
    self.paramFuncs = {0:(lambda x: self.program[self.program[x]]),
                       1:(lambda x: self.program[x])}
  def bambda(self, x):
    return self.paramFuncs[self.opcode.params[x-1]](self.i+x)

  def run(self):
    while True:
      if self.opcode.code == 1:
        in1 = self.bambda(1)
        in2 = self.bambda(2)
        self.program[self.program[self.i+3]] = in1+in2
        self.i += 4
      elif self.opcode.code == 2:
        in1 = self.bambda(1)
        in2 = self.bambda(2)
        self.program[self.program[self.i+3]] = in1*in2
        self.i += 4
      elif self.opcode.code == 3:
        self.program[self.program[self.i+1]] = self.pgmInput[self.pic]
        self.pic += 1
        self.i += 2
      elif self.opcode.code == 4:
        self.pgmOutput += [self.bambda(1)]
        self.i += 2
        # added break because only one output needed
        break
      elif self.opcode.code == 5:
        if self.bambda(1):
          self.i = self.bambda(2)
        else:
          self.i += 3
      elif self.opcode.code == 6:
        if not self.bambda(1):
          self.i = self.bambda(2)
        else:
          self.i += 3
      elif self.opcode.code == 7:
        self.program[self.program[self.i+3]] = int(self.bambda(1) < self.bambda(2))
        self.i += 4
      elif self.opcode.code == 8:
        self.program[self.program[self.i+3]] = int(self.bambda(1) == self.bambda(2))
        self.i += 4
      else:
        break
      self.opcode = Opcode(self.program[self.i])

program = [int(x) for x in stdin.readline().split(',')]

max_signal = None
max_perm = []

for p in permutations([0,1,2,3,4]): 
  signal = 0
  for i in range(5):
    a = Amp(p[i],signal,program)
    a.run()
    signal = a.pgmOutput[0]
  if max_signal is None or signal > max_signal:
    max_signal = signal
    max_perm = p

print(max_signal)
print(max_perm)
