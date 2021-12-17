from sys import stdin

line = stdin.readline().split()
tgt_x = [int(i) for i in line[2][2:-1].split('..')]
tgt_y = [int(i) for i in line[3][2:].split('..')]

tgt_x = range(tgt_x[0],tgt_x[1]+1)
tgt_y = range(tgt_y[0],tgt_y[1]+1)

# minimum x velocity => ( find n where sum(n to 1) first lands in target x )
vel_x_min = 0
while vel_x_min * (vel_x_min + 1) / 2 < tgt_x[0]:
  vel_x_min += 1

# got max y velocity from testing, found any positive initial v_y will
# be going -(v_y + 1) when it reaches position 0 again, and they always
# reach position 0 again. Anything larger will overshoot on way down
# ---- min_tgt_y = -(v_y_max + 1) =>  v_y_max = -(min_tgt_y + 1) ----
vel_y_max = -(tgt_y[0]+1)

# so part 1 answer is the sum of all integers from v_y_max to 1
print('Part 1: ' + str(vel_y_max * (vel_y_max + 1) // 2))

# max x velocity determined by aiming directly for a one shot at max target x
# min y velocity determined by aiming directly for a one shot at min target y
vel_x = range(vel_x_min, tgt_x[-1]+1)
vel_y = range(tgt_y[0], vel_y_max+1)

# brute force with min/max velocity ranges to find what lands in target area
result = 0
for v_x in vel_x:
  for v_y in vel_y:
    v_x_tmp = v_x
    x = 0
    y = 0
    while x < 231 and y > -100:
      if x in tgt_x and y in tgt_y:
        result += 1
        break
      x += v_x_tmp
      if v_x_tmp > 0:
        v_x_tmp -= 1
      y += v_y
      v_y -= 1

print('Part 2: ' + str(result))
