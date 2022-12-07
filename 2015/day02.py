tests = [
    ([2,3,4], 58),
    ([1,1,10], 43)
]

presents = []
with open("day02.txt") as file:
    presents = [[int(c) for c in line.split("x")] for line in file.readlines()]

# def calculate_paper(box):
#     l, w, h = box
#     smallest_side = min(l*w, w*h, h*l)

#     return 2*l*w + 2*w*h + 2*h*l + smallest_side

# for input, expected in tests:
#     output = calculate_paper(input)

#     print(input, output, "expected", expected)
#     assert(output, expected)

# print(sum([calculate_paper(p) for p in presents]))

def calculate_ribbon(box):
    l, w, h = box

    bow = l*w*h

    # print(box, bow)

    if h > l and h > w:        
        # print("height", h, "is largest, l", l, "w", w, 2*w + 2*l)
        return bow + w + w + l + l
    elif l > h and l > w:
        # print("length", l, "is largest, h", h, "w", w, 2*h + 2*w)
        return bow + h + h + w + w
    else:
        # print("width", w, "is largest, h", h, "l", l, 2*h + 2*l)
        return bow + h + h + l + l

tests = [
    ([2,3,4], 34),
    ([2,4,3], 34),
    ([3,2,4], 34),
    ([3,4,2], 34),
    ([4,3,2], 34),
    ([4,2,3], 34),
    ([1,1,10], 14),
    ([1,10,1], 14),
    ([10,1,1], 14)
]

def run_tests(tests, test_method):
    for input, expected in tests:
        output = test_method(input)

        print(input, output, "expected", expected)
        assert(output == expected)

run_tests(tests, calculate_ribbon)
print(sum([calculate_ribbon(p) for p in presents]))