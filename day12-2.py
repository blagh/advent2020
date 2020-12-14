import math

R_COMPASS = "ESWN"
L_COMPASS = "ENWS"


class Nav:
    def __init__(self):
        self.way_x = 10
        self.way_y = 1
        self.x = 0
        self.y = 0
        self.h = "E"


    def move(self, dir, dist):
        if dir == "F":
            print(f"FORWARD {self.h}")
            self.move(self.h, dist)
        elif dir in ["N", "E", "S", "W"]:
            if dir == "N":
                self.x += dist
            elif dir == "E":
                self.y += dist
            elif dir == "S":
                self.x -= dist
            elif dir == "W":
                self.y -= dist
            print(f"{dir} {dist}: ({self.x}, {self.y})")
        elif dir == "R":
            units = int(dist / 90)
            current = R_COMPASS.index(self.h)
            self.h = R_COMPASS[(units + current) % 4]
            print(f"NEW HEADING R {dist}: {self.h}")
        elif dir == "L":
            units = int(dist / 90)
            current = L_COMPASS.index(self.h)
            self.h = L_COMPASS[(units + current) % 4]
            print(f"NEW HEADING L {dist}: {self.h}")

instructions = []

with open("day12input.txt") as file:
    instructions = file.readlines()

nav = Nav()

for line in instructions:
    line = line[:-1]
    if line:
        nav.move(line[0], int(line[1:]))

print(nav.x, nav.y, nav.h)
print(math.fabs(nav.x) + math.fabs(nav.y))
