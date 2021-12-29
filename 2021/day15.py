import sys, heapq, math
from dataclasses import dataclass, field

NEIGHBOURS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_spot(map, x, y):
    if x >= len(map[0]) or y >= len(map) or x < 0 or y < 0:
        return None

    return map[x][y]

def get_unexplored_neighbours(map, x, y):
    nayburs = []

    for (x_diff, y_diff) in NEIGHBOURS:
        n_x, n_y = x + x_diff, y + y_diff
        spot = get_spot(map, n_x, n_y)

        if spot and not spot.explored:
            nayburs.append(spot)

    return nayburs

@dataclass(order=True)
class Spot:
    value: int = field(compare=False)
    x: int = field(compare=False)
    y: int = field(compare=False)
    explored: bool = field(compare=False, default=False)

    min_cost_so_far: int = field(default=math.inf)

    def __eq__(self, other):
        return self.value == other.value and self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.value) + ("*" if self.explored else ".") + str(self.min_cost_so_far)

def print_grid(grid):
    print("\n".join(" ".join(str(s) for s in line) for line in grid), "\n----\n")

def print_bool_grid(grid):
    print("\n".join("".join(["*" if m else "." for m in line]) for line in grid), "\n----\n")

map = []
with open("day15.txt") as file:
    lines = file.readlines()

    grid_size = len(lines)
    map = [[None] * (grid_size * 5) for i in range(grid_size * 5)]

    for y in range(len(lines)):
        for x in range(len(lines[y][:-1])):
            for z_y in range(5):
                for z_x in range(5):
                    x_pos = x + z_x * grid_size
                    y_pos = y + z_y * grid_size

                    value = int(lines[x][y])
                    z = z_x + z_y
                    if z > 0:
                        value = value + z
                        if value > 9:
                            value = (value % 9)

                    map[x_pos][y_pos] = Spot(value, x_pos, y_pos)

print_grid(map)

fringe = []
def visit(map, spot, fringe):
    print("next", repr(spot))
    spot.explored = True

    neighbours = get_unexplored_neighbours(map, spot.x, spot.y)

    print("  new neighbours", neighbours)

    for n in neighbours:
        cost = spot.min_cost_so_far + int(n.value)

        if cost < n.min_cost_so_far:
            n.min_cost_so_far = cost

        if n not in fringe:
            heapq.heappush(fringe, n)

    # print("  fringe", fringe)
    # print_grid(map)


map[0][0].min_cost_so_far = 0
heapq.heappush(fringe, map[0][0])

while fringe:
    next = heapq.heappop(fringe)

    if next == map[-1][-1]:
        print(" we're done!")
        break

    visit(map, next, fringe)

path_cost = map[-1][-1]
print_grid(map)
print(path_cost)
