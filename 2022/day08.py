def run_tests(tests, test_method):
    for input, expected in tests:
        output = test_method(input)

        print(input, output, "expected", expected)
        assert(output == expected)


with open("day08input.txt") as file:
    for line in file.readlines():
        pass