def run_test(input, expected, test_method):
    actual = test_method(input)

    print(input, "\nactual:", actual, "\nexpect:", expected)
    assert(expected == actual)

def run_tests(tests, test_method):
    for input, expected in tests:
        run_test(input, expected, test_method)

def print_2d_array(array):
    print("\n".join([" ".join([str(i).ljust(6) for i in line]) for line in array]), "\n\n\n")

def count_vis(trees, i, j, i_inc, j_inc):
    count = 0

    # print(i_inc, j_inc)

    i_diff, j_diff = i_inc, j_inc
    while i + i_diff >= 0 and i + i_diff < len(trees) and \
          j + j_diff >= 0 and j + j_diff < len(trees[i]) and \
          trees[i][j] > trees[i + i_diff][j + j_diff]:
        
        # print(i, j, ":", trees[i][j], ",", i+i_diff, j+j_diff, ":", trees[i+i_diff][j+j_diff])
        count += 1
        i_diff += i_inc
        j_diff += j_inc

    if i + i_diff >= 0 and i + i_diff < len(trees) and \
       j + j_diff >= 0 and j + j_diff < len(trees[i]):
        # print(i, j, ":", trees[i][j], ",", i+i_diff, j+j_diff, ":", trees[i+i_diff][j+j_diff])
        count += 1
    # else:
    #     print('the edge 102.7fm')

    # print("return:", count)

    return count

def get_vis(trees):
    vis = [[0 for tree in line] for line in trees]

    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            vis[i][j] = count_vis(trees, i, j, +1, 0) * \
                        count_vis(trees, i, j, -1, 0) * \
                        count_vis(trees, i, j, 0, +1) * \
                        count_vis(trees, i, j, 0, -1)

            print_2d_array(vis)
    return max(max(line for line in array) for array in vis)

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

run_test(test_trees, 8, get_vis)

# max_vis = get_vis(trees)
# print(max_vis)