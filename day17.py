
from functools import reduce

INACTIVE = "."
ACTIVE = "#"

map = []

def expand(map):
    max_x = len(map)
    max_y = len(map[0])
    planes = [
        [0, 0, 1, 0, max_x],
        [0, 0, 0, 1, max_y],
        [0, max_y - 1, 1, 0, max_x],
        [max_x - 1, 0, 0, 1, max_y]
    ]

    print_stuff(map)

    should_add_border = False
    new_map = map
    for plane in planes:
        count = count_plane(map, *plane)
        if count > 0:
            should_add_border = True

    if should_add_border:
        new_map = add_border(map)

    return new_map

def count_plane(map, x, y, x_dir, y_dir, max):
    count = 0
    for diff in range(max):
        if map[x + x_dir * diff][y + y_dir * diff] == ACTIVE:
            count += 1
    return count


def add_border(map):
    max_x = len(map) + 2
    max_y = len(map[0]) + 2

    new_map = [[INACTIVE for y in range(max_y)] for x in range(max_x)]
    for x in range(len(map)):
        row = map[x]
        for y in range(len(row)):
            new_map[x+1][y+1] = map[x][y]

    return new_map


def step(map):
    new_map = []
    count_map = get_counts(map)

    for row in range(len(map)):
        new_row = ""
        for col in range(len(map[row])):
            new_row += get_spot(map, count_map, row, col)
        new_map.append(new_row)
    return new_map

def get_counts(map):
    counts = [[[0 for i in range(len(map[0][0]))] for i in range(len(map[0]))] for i in range(len(map))]
    for row in range(len(map)):
        for col in range(len(map[row])):
            for pln in range(len(map[row][col])):
                if map[row][col][pln] == ACTIVE:
                    mark(map, counts, row, col, pln, -1, -1, -1)
                    mark(map, counts, row, col, pln, -1, -1, 0)
                    mark(map, counts, row, col, pln, -1, -1, +1)

                    mark(map, counts, row, col, pln, -1, 0, -1)
                    mark(map, counts, row, col, pln, -1, 0, 0)
                    mark(map, counts, row, col, pln, -1, 0, +1)

                    mark(map, counts, row, col, pln, -1, +1, -1)
                    mark(map, counts, row, col, pln, -1, +1, 0)
                    mark(map, counts, row, col, pln, -1, +1, +1)

                    mark(map, counts, row, col, pln, 0, -1, -1)
                    mark(map, counts, row, col, pln, 0, -1, 0)
                    mark(map, counts, row, col, pln, 0, -1, +1)

                    # mark(map, counts, row, col, 0, 0, 0)
                    mark(map, counts, row, col, pln, 0, +1, -1)
                    mark(map, counts, row, col, pln, 0, +1, 0)
                    mark(map, counts, row, col, pln, 0, +1, +1)

                    mark(map, counts, row, col, pln, +1, -1, -1)
                    mark(map, counts, row, col, pln, +1, -1, 0)
                    mark(map, counts, row, col, pln, +1, -1, +1)

                    mark(map, counts, row, col, pln, +1, 0, -1)
                    mark(map, counts, row, col, pln, +1, 0, 0)
                    mark(map, counts, row, col, pln, +1, 0, +1)

                    mark(map, counts, row, col, pln, +1, +1, -1)
                    mark(map, counts, row, col, pln, +1, +1, 0)
                    mark(map, counts, row, col, pln, +1, +1, +1)


    print_counts(counts)
    return counts

def mark(map, counts, row, col, pln, x_dir, y_dir, z_dir):
    next_x = row + x_dir
    next_y = col + y_dir
    next_z = pln + z_dir
    if next_x >= 0 and next_x < len(map) \
      and next_y >= 0 and next_y < len(map[row]) \
      and next_z >= 0 and next_z < len(map[row][col]):
      counts[next_x][next_y][next_z] += 1

    # print_counts(counts)


def get_spot(map, counts, row, col):
    spot = map[row][col]
    surround_count = counts[row][col]
    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
    if spot == INACTIVE and surround_count == 3:
        return ACTIVE
    if spot == ACTIVE and (surround_count != 2 or surround_count != 3):
        return INACTIVE
    return spot

def check_equal(old, new):
    for n in range(len(old)):
        for m in range(len(old[n])):
            if old[n][m] != new[n][m]:
                print(n, old[n], new[n])
                return False
    return True

def print_counts(these_counts):
    stringed = "\n\n".join("\n".join([str(i) for i in row]) for row in these_counts)
    print(stringed + "\n")

def print_stuff(this_map):
    stringed = "\n\n".join("\n".join(["".join(i) for i in row]) for row in this_map)

    active_count = reduce(lambda a, b: a + 1 if b == ACTIVE else a, stringed, 0)
    print(stringed, active_count)
    print()

    return active_count

with open("day17input.txt") as file:
    map = file.readlines()
    map = [[[n for n in m[:-1]] for m in map]] # trim newlines

n = 0
max = 7
map = expand(map)
print_stuff(map)

while n < max:
    new_map = step(map)
    active_count = print_stuff(new_map)

    if active_count == 0:
        print("all dead :(")
        print(f"it took {n} rounds")
        break

    if new_map == map:
        print("no changes!!")
        print(f"it took {n} rounds")
        break
    map = expand(new_map)
    n += 1
    if n == max:
        print("and we're done !!")
