def run_test(input, expected, test_method):
    actual = test_method(input)

    print(input, "\nactual:", actual, "\nexpect:", expected)
    assert(expected == actual)

def run_tests(tests, test_method):
    for input, expected in tests:
        run_test(input, expected, test_method)

def print_2d_array(array):
    print("\n".join(["".join(line) for line in array]), "\n\n\n")

with open("input.txt") as file:
    for line in file.readlines():
        pass