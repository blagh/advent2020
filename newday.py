def run_tests(tests, test_method):
    for input, expected in tests:
        output = test_method(input)

        print(input, output, "expected", expected)
        assert(output == expected)


with open("input.txt") as file:
    for line in file.readlines():
        pass