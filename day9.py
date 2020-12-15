lines = []

with open("day9input.txt") as file:
    lines = file.readlines()

lines = [int(l[:-1]) for l in lines]

PREAMBLE = 25

for i in range(PREAMBLE, len(lines)):
    line = lines[i]
    preamble = lines[i-PREAMBLE:i]
    print(line, preamble)

    combo_found = False
    for j in range(PREAMBLE):
        for k in range(PREAMBLE):
            print(preamble[j], preamble[k])

            if j != k and preamble[j] + preamble[k] == line:
                combo_found = True
                break

        if combo_found:
            break

    if not combo_found:
        print(line)
        break
