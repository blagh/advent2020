lines = []

with open("day03.txt") as file:
    lines = [l.rstrip() for l in file.readlines()]

print(lines)
line_len = len(lines[0])

def count_ones(position, lines):
    total_lines = len(lines)
    one_count = 0

    for l in lines:
        if l[i] == "1":
            one_count += 1

    return one_count

def filter_lines(req_char, position, lines):
    new_lines = []
    for l in lines:
        if l[position] == req_char:
            new_lines.append(l)

    return new_lines

def filter_o2_lines(position, lines):
    if len(lines) == 1:
        return lines

    one_count = count_ones(position, lines)
    req_char = "1" if one_count >= len(lines) / 2 else "0"

    print("o2", position, one_count, req_char)
    return filter_lines(req_char, position, lines)

def filter_co2_lines(position, lines):
    if len(lines) == 1:
        return lines

    one_count = count_ones(position, lines)
    req_char = "0" if one_count >= len(lines) / 2 else "1"

    print("co2", position, one_count, req_char)
    return filter_lines(req_char, position, lines)


o2_cands = lines
co2_cands = lines

print(o2_cands, co2_cands)

for i in range(line_len):
    o2_cands = filter_o2_lines(i, o2_cands)
    co2_cands = filter_co2_lines(i, co2_cands)

    print(o2_cands, co2_cands)

o2_rate = int(o2_cands[0], base=2)
co2_rate = int(co2_cands[0], base=2)

print(o2_rate, co2_rate)
print(o2_rate * co2_rate)
