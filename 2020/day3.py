map = []


with open("day3input.txt") as file:
    map = file.readlines()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def set_color(pretty, p, is_good):
    color = bcolors.OKGREEN if is_good else bcolors.FAIL
    return pretty[:p] + color + pretty[p] + bcolors.ENDC + pretty[p+1:]

def check_slope(map, x_diff):
    x = 0
    y = 0
    tree_count = 0

    for line in map:
        line = line[:-1] # strip newline

        map_x = x % len(line)
        is_tree = line[map_x] == "#"
        print(f'{y:03}', set_color(line, map_x, is_tree) * 3, x, map_x)

        if is_tree:
            tree_count += 1
        x += x_diff
        y += 1

    return tree_count

tree_1 = check_slope(map, 1)
print(tree_1)
tree_2 = check_slope(map, 3)
print(tree_2)
tree_3 = check_slope(map, 5)
print(tree_3)
tree_4 = check_slope(map, 7)
print(tree_4)
tree_5 = check_slope(map[::2], 1)
print(tree_5)

print(tree_1 * tree_2 * tree_3 * tree_4 * tree_5)
