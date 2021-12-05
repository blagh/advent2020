import itertools

class Point:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

def inclusive_range(one, two):
    if one <= two:
        return range(one, two+1, 1)
    else:
        return range(one, two-1, -1)

class Line:

    def __init__(self, one, two):
        self.one = Point(*one.split(","))
        self.two = Point(*two.split(","))

    def is_straight(self):
        return self.one.x == self.two.x or self.one.y == self.two.y

    def draw(self, map):
        x_range = inclusive_range(self.one.x, self.two.x)
        y_range = inclusive_range(self.one.y, self.two.y)

        if self.is_straight():
            for x in x_range:
                for y in y_range:
                    map[x][y] += 1
        else:
            for (x, y) in itertools.zip_longest(x_range, y_range):
                map[x][y] += 1

    def __str__(self):
        is_straight = "✅" if self.is_straight() else "✖"

        return "{},{} -> {}, {} {}\n".format(self.one.x, self.one.y, self.two.x, self.two.y, is_straight)

    def __repr__(self):
        is_straight = "✅" if self.is_straight() else "✖"

        return "{},{} -> {}, {} {}\n".format(self.one.x, self.one.y, self.two.x, self.two.y, is_straight)

empty = 0
grid_size = 1000
map = [[empty] * grid_size for i in range(grid_size)]

lines = []
with open("day05.txt") as file:
    file_lines = file.readlines()
    for l in file_lines:
        points = l.split(" -> ")
        line = Line(*points)

        # part 1
        # if line.is_straight():
        #   line.draw(map)

        # part 2
        line.draw(map)

        print(line)

map_str = ""
for l in map:
    for c in l:
        map_str += str(c)
    map_str += "\n"
print(map_str)

count = 0
for x, y in itertools.product(range(grid_size), range(grid_size)):
    if map[x][y] > 1:
        count += 1
print(count)
