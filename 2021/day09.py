map = []

with open("day09.txt") as file:
    map = [o[:-1] for o in file.readlines()]

print("\n".join(m for m in map))

low_points = []
low_sum = 0
for i in range(len(map)):
    for j in range(len(map[i])):

        cell = map[i][j]
        lowest = True
        above = None
        below = None
        leftt = None
        right = None

        if i < len(map) - 1:
            below = map[i+1][j]
            if map[i+1][j] <= cell:
                lowest = False

        if i > 0:
            above = map[i-1][j]
            if map[i-1][j] <= cell:
                lowest = False

        if j < len(map[i]) - 1:
            right = map[i][j+1]
            if map[i][j+1] <= cell:
                lowest = False

        if j > 0:
            leftt = map[i][j-1]
            if map[i][j-1] <= cell:
                lowest = False

        if lowest:
            print(cell, ":", above, below, leftt, right)
            low_points.append((i, j))
            low_sum += int(cell) + 1

print(low_points, low_sum)

row_len = len(map[i])
col_len = len(map)
visited = [["."] * row_len for i in range(col_len)]

def basin_size(i, j, depth):
    print(" " * depth, "checking (", i, j, ")")

    if i >= len(map) or j >= len(map[i]) or i < 0 or j < 0:
        return 0


    if map[i][j] == "9" or visited[i][j] == "*":
        if map[i][j] == "9":
            visited[i][j] = "^"

        return 0

    visited[i][j] = "*"

    return basin_size(i+1, j, depth + 1) + basin_size(i-1, j, depth + 1) + basin_size(i, j+1, depth + 1) + basin_size(i, j-1, depth + 1) + 1

basins = []
for point in low_points:
    size = basin_size(point[0], point[1], 0)

    print("done")
    print("\n".join("".join(m) for m in visited), "\n----\n")

    basins.append(size)

print(basins)

max_1 = max(basins)
basins.remove(max_1)
max_2 = max(basins)
basins.remove(max_2)
max_3 = max(basins)

print(max_1 * max_2 * max_3)
