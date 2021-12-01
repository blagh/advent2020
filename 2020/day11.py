
FLOOR = "."
EMPTY_SEAT = "L"
OCCUPIED = "#"

map = []

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
    counts = [[0 for i in range(len(map[0]))] for i in range(len(map))]
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == OCCUPIED:
                mark_until(map, counts, row, col, -1, -1)
                mark_until(map, counts, row, col, -1, 0)
                mark_until(map, counts, row, col, -1, +1)
                mark_until(map, counts, row, col, 0, -1)
                # mark_until(map, counts, row, col, 0, 0)
                mark_until(map, counts, row, col, 0, +1)
                mark_until(map, counts, row, col, +1, -1)
                mark_until(map, counts, row, col, +1, 0)
                mark_until(map, counts, row, col, +1, +1)

    print_counts(counts)
    return counts

def mark_until(map, counts, row, col, x_dir, y_dir):
    next_x = row + x_dir
    next_y = col + y_dir
    if next_x >= 0 and next_x < len(map) \
      and next_y >= 0 and next_y < len(map[row]):
      counts[next_x][next_y] += 1


def get_spot(map, counts, row, col):
    spot = map[row][col]
    surround_count = counts[row][col]
    # # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    # # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty
    if spot == EMPTY_SEAT and surround_count == 0:
        return OCCUPIED
    if spot == OCCUPIED and surround_count >= 4:
        return EMPTY_SEAT
    return spot

with open("day11input.txt") as file:
    map = file.readlines()
    map = [m[:-1] for m in map] # trim newlines

def check_equal(old, new):
    for n in range(len(old)):
        for m in range(len(old[n])):
            if old[n][m] != new[n][m]:
                print(n, old[n], new[n])
                return False
    return True

def print_counts(these_counts):
    stringed = "\n".join("".join([str(i) for i in row]) for row in these_counts)
    print(stringed + "\n")

def print_stuff(this_map):
    stringed = "\n".join(this_map)
    print(stringed)
    print(len(list(filter(lambda c: c == OCCUPIED, stringed))))

n = 0
max = 499
while n < max:
    new_map = step(map)
    if new_map == map:
        print_stuff(new_map)
        print("it's done!!")
        print(f"it took {n} rounds")
        break
    map = new_map
    n += 1
    if n == max:
        print_stuff(map)
        print_stuff(new_map)
        print("early break !!")
