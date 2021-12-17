# brute force after manual calc for part 1
#
# 20 is minimum x velocity => ( n * (n + 1) / 2 in range 201 .. 230 )
#
# got max y velocity from testing, found any positive initial v_y will
# be going -(v_y + 1) when it reaches position 0 again, and they always
# reach position 0 again. So max y velocity must be 98. Anything larger
# will overshoot on way down
# ---- min_tgt_y = -99  =>  -(v_y_max + 1) = -99  =>  v_y_max = 98 ----
# so part 1 answer is 98 * 99 / 2, the sum of all integers from 98 to 1, 4851
#
# max x velocity determined by aiming directly for a one shot at max target x
# min y velocity determined by aiming directly for a one shot at min target y

tgt_x = range(201,231)
tgt_y = range(-99,-64)

x_vel = range(20, 231)
y_vel = range(-99, 99)

result = 0
for v_x in x_vel:
  for v_y in y_vel:
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

print(result)
