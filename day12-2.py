from math import sin, cos, radians, fabs

R_COMPASS = "ESWN"
L_COMPASS = "ENWS"

class Nav:
    def __init__(self):
        self.way_x = 10
        self.way_y = 1
        self.x = 0
        self.y = 0

    def move(self, dir, dist):
        if dir == "F":
            self.x += self.way_x * dist
            self.y += self.way_y * dist
            print(f"\nFORWARD {dist} ({self.way_x}, {self.way_y}): ({self.x}, {self.y})")

        elif dir in ["N", "E", "S", "W"]:
            if dir == "N":
                self.way_y += dist
            elif dir == "E":
                self.way_x += dist
            elif dir == "S":
                self.way_y -= dist
            elif dir == "W":
                self.way_x -= dist
            print(f"WAYPOINT {dir} {dist}: ({self.way_x}, {self.way_y})")
        elif dir in ["R", "L"]:
            rads = radians(dist)
            s = sin(rads)
            c = cos(rads)
            x = self.way_x
            y = self.way_y

            if dir == "R":
                self.way_x = round(x * c + y * s);
                self.way_y = round(-x * s + y * c);
                print(f"WAYPOINT R {dist}: ({self.way_x}, {self.way_y})")
            elif dir == "L":
                self.way_x = round(x * c - y * s);
                self.way_y = round(x * s + y * c);
                print(f"WAYPOINT L {dist}: ({self.way_x}, {self.way_y})")

instructions = []

with open("day12input.txt") as file:
    instructions = file.readlines()

nav = Nav()

for line in instructions:
    line = line[:-1]
    if line:
        nav.move(line[0], int(line[1:]))

print(nav.x, nav.y, nav.way_x, nav.way_y)
print(fabs(nav.x) + fabs(nav.y))
