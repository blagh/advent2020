def run_test(input, expected, test_method):
    actual = test_method(input)

    print(input, "\nactual:", actual, "\nexpect:", expected)
    assert(expected == actual)

def run_tests(tests, test_method):
    for input, expected in tests:
        run_test(input, expected, test_method)

def print_2d_array(array):
    print("\n".join(["".join(line) for line in array]), "\n\n\n")

def get_vis(trees):
    vis = [[' ' for t in tree] for tree in trees]

    for i in range(len(trees)):
        max = trees[i][0]
        for j in range(len(trees[i])):
            if i == 0 or j == 0 or trees[i][j] > max:
                max = trees[i][j]
                vis[i][j] = trees[i][j]
                print_2d_array(vis)

            if max == 9:
                break

    for i in range(len(trees)):
        max = trees[0][i]
        for j in range(len(trees[i])):
            if i == 0 or j == 0 or trees[j][i] > max:
                max = trees[j][i]
                vis[j][i] = trees[j][i]
                print_2d_array(vis)

            if max == 9:
                break

    for i in range(len(trees) - 1, -1, -1):
        max = trees[i][len(trees[i]) - 1]
        for j in range(len(trees[i]) - 1, -1, -1):

            if i == len(trees) - 1 or j == len(trees) - 1 or trees[i][j] > max: 
                max = trees[i][j]
                vis[i][j] = trees[i][j]
                print_2d_array(vis)

            if max == 9:
                break

    for i in range(len(trees) - 1, -1, -1):
        max = trees[len(trees) - 1][i]

        for j in range(len(trees[i]) - 1, -1, -1):
            if i == len(trees[i]) - 1 or j == len(trees[i]) - 1 or trees[j][i] > max:
                max = trees[j][i]
                vis[j][i] = trees[j][i]
                print_2d_array(vis)

            if max == 9:
                break

    return sum(len(list(filter(lambda v: v != " ", line))) for line in vis), vis

expected = [
    ['3', '0', '3', '7', '3'],
    ['2', '5', '5', ' ', '2'],
    ['6', '5', ' ', '3', '2'],
    ['3', ' ', '5', ' ', '9'],
    ['3', '5', '3', '9', '0']
]

with open("day08test.txt") as file:
    test_trees = [line.strip() for line in file.readlines()]

with open("day08input.txt") as file:
    trees = [line.strip() for line in file.readlines()]

run_test(test_trees, (21, expected), get_vis)

(count, vis) = get_vis(trees)
print(count)