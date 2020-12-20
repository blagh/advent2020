lines = []

with open("day10input.txt") as file:
    lines = file.readlines()

lines = [int(l[:-1]) for l in lines]
lines = sorted(lines)
lines = lines + [lines[-1] + 3]



def compatible(n, lines):
    return list(filter(lambda x: x > n and x <= n+3, lines))
nodes = {l: compatible(l, lines) for l in lines}

def part_1(lines):

    lines = lines[:] + [lines[-1] + 3]
    one_diffs = 0
    three_diffs = 0
    prev_number = 0
    for n in lines:
        if n - prev_number == 1:
            one_diffs += 1
        elif n - prev_number == 3:
            three_diffs += 1
        prev_number = n
    print(one_diffs, three_diffs)

part_1(lines)
print(nodes)
