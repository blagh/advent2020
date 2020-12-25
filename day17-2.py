
from functools import reduce
from itertools import product

INACTIVE = "."
ACTIVE = "#"

map = []

def expand(map):
    max_x = len(map)
    max_y = len(map[0])
    max_z = len(map[0][0])
    max_a = len(map[0][0][0])
    planes = [
        [0, 0, 0, 0, max_x, max_y, max_z, 1],
        [0, 0, 0, 0, max_x, max_y, 1, max_a],
        [0, 0, 0, 0, max_x, 1, max_z, max_a],
        [0, 0, 0, 0, 1, max_y, max_z, max_a],

        [0, 0, 0, max_a-1, max_x, max_y, max_z, max_a],
        [0, 0, max_z-1, 0, max_x, max_y, max_z, max_a],
        [0, max_y-1, 0, 0, max_x, max_y, max_z, max_a],
        [max_x-1, 0, 0, 0, max_x, max_y, max_z, max_a]
    ]

    should_add_border = False
    new_map = map
    for plane in planes:
        should_add_border = should_expand(map, *plane)
        if should_add_border:
            print("expanding ~~~")
            break

    if should_add_border:
        new_map = add_border(map)
        print_stuff(new_map)

    return new_map

def should_expand(map, x, y, z, a, max_x, max_y, max_z, max_a):
    for x_pos in range(x, max_x - x):
        for y_pos in range(y, max_y - y):
            for z_pos in range(z, max_z - z):
                for a_pos in range(a, max_a - a):
                    if map[x_pos][y_pos][z_pos][a_pos] == ACTIVE:
                        return True

    return False


def add_border(map):
    max_x = len(map) + 2
    max_y = len(map[0]) + 2
    max_z = len(map[0][0]) + 2
    max_a = len(map[0][0][0]) + 2

    new_map = [[[[INACTIVE for a in range(max_a)] for z in range(max_z)] for y in range(max_y)] for x in range(max_x)]
    for x in range(len(map)):
        for y in range(len(map[x])):
            for z in range(len(map[x][y])):
                for a in range(len(map[x][y][z])):
                    new_map[x+1][y+1][z+1][a+1] = map[x][y][z][a]

    return new_map


def step(map):
    new_map = []
    count_map = get_counts(map)

    for row in range(len(map)):
        new_pln = []
        for col in range(len(map[row])):
            new_row = []
            for pln in range(len(map[row][col])):
                new_tim = []
                for tim in range(len(map[row][col][pln])):
                    spot = map[row][col][pln][tim]
                    active_count = count_map[row][col][pln][tim]
                    new_tim.append(get_spot(spot, active_count))
                new_row.append(new_tim)
            new_pln.append(new_row)
        new_map.append(new_pln)
    return new_map

def get_counts(map):
    counts = [[[[0 for i in range(len(map[0][0][0]))] for i in range(len(map[0][0]))] for i in range(len(map[0]))] for i in range(len(map))]
    surroundings = list(product([-1, 0, 1], repeat=4))

    for row in range(len(map)):
        for col in range(len(map[row])):
            for pln in range(len(map[row][col])):
                for tim in range(len(map[row][col][pln])):
                    if map[row][col][pln][tim] == ACTIVE:
                        for surround in surroundings:
                            if surround != (0, 0, 0, 0):
                                mark(counts, row, col, pln, tim, *surround)

    print_counts(counts)
    return counts

def mark(counts, row, col, pln, tim, x_dir, y_dir, z_dir, a_dir):
    next_x = row + x_dir
    next_y = col + y_dir
    next_z = pln + z_dir
    next_a = tim + a_dir
    counts[next_x][next_y][next_z][next_a] += 1

def get_spot(spot, surround_count):
    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
    if spot == INACTIVE and surround_count == 3:
        return ACTIVE
    if spot == ACTIVE and surround_count not in [2,3]:
        return INACTIVE
    return spot

def check_equal(old, new):
    for n in range(len(old)):
        for m in range(len(old[n])):
            if old[n][m] != new[n][m]:
                print(n, old[n], new[n])
                return False
    return True

def print_counts(this_map):
    stringed = ""
    for a in range(len(this_map[0][0][0])):
        for x in range(len(this_map)):
            for z in range(len(this_map[0][0])):
                for y in range(len(this_map[0])):
                    stringed += f"{this_map[x][y][z][a]:2} "
                stringed += " "
            stringed += "\n"
        stringed += "---------\n"
    print(stringed)

def print_stuff(this_map):
    stringed = ""
    for a in range(len(this_map[0][0][0])):
        for x in range(len(this_map)):
            for z in range(len(this_map[0][0])):
                for y in range(len(this_map[0])):
                    stringed += this_map[x][y][z][a]
                stringed += " "
            stringed += "\n"
        stringed += "---------\n"

    active_count = reduce(lambda a, b: a + 1 if b == ACTIVE else a, stringed, 0)
    print(stringed + f"count: {active_count}")
    print()

    return active_count

with open("day17input.txt") as file:
    map = file.readlines()
    map = [[[[n]] for n in m[:-1]] for m in map] # trim newlines

n = 0
max = 6
print_stuff(map)

map = expand(map)

while n <= max:
    new_map = step(expand(map))
    active_count = print_stuff(new_map)

    if active_count == 0:
        print("all dead :(")
        print(f"it took {n} rounds")
        break

    if new_map == map:
        print("no changes!!")
        print(f"it took {n} rounds")
        break
    map = new_map
    n += 1
    if n == max:
        print("and we're done !!")
        break
