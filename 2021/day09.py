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
            low_points.append(cell)
            low_sum += int(cell) + 1

print(low_points, low_sum)
