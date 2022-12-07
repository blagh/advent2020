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

    print(box, bow)

    if h > l and h > w:        
        print("height", h, "is largest, l", l, "w", w, 2*w + 2*l)
        return bow + 2*w + 2*l
    elif l > h and l > w:
        print("length", l, "is largest, h", h, "w", w, 2*h + 2*w)
        return bow + 2*h + 2*w
    else:
        print("width", w, "is largest, h", h, "l", l, 2*h + 2*l)
        return bow + 2*h + 2*l

tests = [
    ([2,3,4], 34),
    ([1,1,10], 14),
    ([10,9,8], 754),
    ([15,15,7], 1619)
]

for input, expected in tests:
    output = calculate_ribbon(input)

    print(input, output, "expected", expected)
    assert(output == expected)

ribbon_sum = 0
for p in presents:
    ribbon = calculate_ribbon(p)
    ribbon_sum += ribbon

    print(ribbon, ribbon_sum)

print(ribbon_sum)