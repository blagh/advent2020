lines = []

with open("day03.txt") as file:
    lines = [l.rstrip() for l in file.readlines()]

print(lines)
line_len = len(lines[0])

def count_ones(position, lines):
    return len(list(filter(lambda l: l[position] == "1", lines)))

def filter_lines(position, one_char, zero_char, sensor, lines):
    if len(lines) == 1:
        return lines

    one_count = count_ones(position, lines)
    req_char = one_char if one_count >= len(lines) / 2 else zero_char

    print(sensor, position, one_count, req_char)

    return list(filter(lambda l: l[position] == req_char, lines))

o2_cands = lines
co2_cands = lines

print(o2_cands, co2_cands)

for i in range(line_len):
    o2_cands = filter_lines(i, "1", "0", "o2", o2_cands)
    co2_cands = filter_lines(i, "0", "1", "co2", co2_cands)

    print(o2_cands, co2_cands)

o2_rate = int(o2_cands[0], base=2)
co2_rate = int(co2_cands[0], base=2)

print(o2_rate, co2_rate)
print(o2_rate * co2_rate)
print(o2_rate * co2_rate == 1353024)
