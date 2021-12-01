import math

R_COMPASS = "ESWN"
L_COMPASS = "ENWS"


def move(dir, dist, x, y, h):
    if dir == "F":
        print(f"FORWARD {h}")
        (x, y, h) = move(h, dist, x, y, h)
    elif dir in ["N", "E", "S", "W"]:
        if dir == "N":
            x += dist
        elif dir == "E":
            y += dist
        elif dir == "S":
            x -= dist
        elif dir == "W":
            y -= dist
        print(f"{dir} {dist}: ({x}, {y})")
    elif dir == "R":
        units = int(dist / 90)
        current = R_COMPASS.index(h)
        h = R_COMPASS[(units + current) % 4]
        print(f"NEW HEADING R {dist}: {h}")
    elif dir == "L":
        units = int(dist / 90)
        current = L_COMPASS.index(h)
        h = L_COMPASS[(units + current) % 4]
        print(f"NEW HEADING L {dist}: {h}")

    return (x, y, h)

instructions = []

with open("day12input.txt") as file:
    instructions = file.readlines()

x = 0
y = 0
h = "E"

for line in instructions:
    line = line[:-1]
    if line:
        (x, y, h) = move(line[0], int(line[1:]), x, y, h)

print(x, y, h)
print(math.fabs(x) + math.fabs(y))
