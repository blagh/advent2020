lines = []

with open("day10input.txt") as file:
    lines = file.readlines()

lines = [int(l[:-1]) for l in lines]
lines = sorted(lines)
lines = [0] + lines + [lines[-1] + 3]

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


def compatible(n, lines):
    return list(filter(lambda x: x > n and x <= n+3, lines))


sequences = {}

def count_sequences(n, nodes, depth=0):
    if n in sequences:
        return sequences[n]

    children = nodes[n]

    if len(children) == 0:
        return 1

    if len(children) == 1:
        count = count_sequences(children[0], nodes, depth)
        sequences[n] = count

    total = 0
    for c in children:
        total += count_sequences(c, nodes, depth+1)
    print(" "*depth + f"recurse many: {total}")
    sequences[n] = total
    return total

nodes = {l: compatible(l, lines) for l in lines}
print(nodes)
print(count_sequences(0, nodes))
