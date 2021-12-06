from sys import stdin

x = 146810
total = 0

while x < 612565:
  y = [c for c in str(x)]
  if y == sorted(str(x)):
    state = 0
    prevC = ''
    for c in y:
      # debug
      #if x == 222233:
      #  print("state: "+str(state))
      #  print("prevC: "+str(prevC))
      #  print("c: "+c)
      if state == 0:
        prevC = c
        state = 1
      elif state == 1:
        if c == prevC:
          state = 2
        else:
          prevC = c
      elif state == 2:
        if c != prevC:
          break
        else:
          state = 3
      else:
        if c != prevC:
          prevC = c
          state = 1
    if state == 2:
      total += 1
  x += 1

print(total)
