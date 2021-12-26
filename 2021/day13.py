grid_x_size = 2000
grid_y_size = 2000

coords = True
grid = [[False] * grid_x_size for g in range(grid_y_size)]
folds = []

def print_grid(grid):
    print("\n".join("".join(["*" if m else "." for m in line]) for line in grid), "\n----\n")

with open("day13.txt") as file:
    for line in file.readlines():
        if not line[:-1]:
            coords = False
            continue

        if coords:
            (y, x) = line[:-1].split(",")
            grid[int(x)][int(y)] = True
        else:
            fold = (line[11], int(line[13:-1]))
            folds.append(fold)

print_grid(grid)
print(folds)

def fold_y(grid, pos):
    top_half = grid[0:pos]
    bottom_half = grid[pos+1:]

    print("top")
    print_grid(top_half)
    print("bottom")
    print_grid(bottom_half)

    for i in range(len(bottom_half)):
        if i >= len(top_half):
            continue

        for j in range(len(bottom_half[i])):
            nega_i = i * -1 - 1
            top_half[nega_i][j] = top_half[nega_i][j] or bottom_half[i][j]

    return top_half

def fold_x(grid, pos):
    left_half = [line[0:pos] for line in grid]
    right_half = [line[pos+1:] for line in grid]

    print("left")
    print_grid(left_half)
    print("right")
    print_grid(right_half)

    for i in range(len(left_half)):
        for j in range(len(right_half[i])):
            if j >= len(left_half[i]):
                continue

            nega_j = j * -1 - 1
            left_half[i][nega_j] = left_half[i][nega_j] or right_half[i][j]

    return left_half

def sum_all(grid):
    s = 0
    for line in grid:
        for o in line:
            s += 1 if o else 0
    return s

for f in folds:
    if f[0] == "x":
        grid = fold_x(grid, f[1])
    else:
        grid = fold_y(grid, f[1])

print("result!")
print_grid(grid)
print(sum_all(grid))
