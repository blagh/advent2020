# target area: x=248..285, y=-85..-56
# target area: x=20..30, y=-10..-5

# X_MIN = 20
# X_MAX = 30
# Y_MIN = -10
# Y_MAX = -5

X_MIN = 248
X_MAX = 285
Y_MIN = -85
Y_MAX = -56

def simulate(x_speed, y_speed):
    x_pos, y_pos = 0, 0

    max_y_pos = 0

    while x_pos <= X_MAX and y_pos >= Y_MIN:

        if x_pos >= X_MIN and y_pos <= Y_MAX:
            # we hit it!
            print("hit!", x_pos, y_pos, max_y_pos)
            return True, max_y_pos

        x_pos += x_speed
        y_pos += y_speed

        if x_speed > 0:
            x_speed -= 1

        if x_speed < 0:
            x_speed += 1

        y_speed -= 1

        if y_pos > max_y_pos:
            max_y_pos = y_pos

    # we hit no such thing
    print("no hit :(", x_pos, y_pos)
    return False, None

max_y_pos = 0
good_x = 0
good_y = 0
count = 0

for x in range(-300, 300):
    for y in range(-100, 100):
        print(x, y)
        hit, max_y = simulate(x, y)

        if hit:
            count += 1

        if hit and max_y > max_y_pos:
            max_y_pos = max_y
            good_x = x
            good_y = y

print("and in the end...")
print(max_y_pos, good_x, good_y)
print(count)
