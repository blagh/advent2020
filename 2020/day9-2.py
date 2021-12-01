# INVALID_NUMBER = 127
INVALID_NUMBER = 22477624

lines = []

with open("day9input.txt") as file:
    lines = file.readlines()

lines = [int(l[:-1]) for l in lines]

lower_bound = 0
upper_bound = 1

for i in range(len(lines)):
    section = lines[lower_bound:upper_bound]
    summ = sum(section)

    if summ < INVALID_NUMBER:
        upper_bound += 1
    elif summ > INVALID_NUMBER:
        lower_bound += 1
    elif summ == INVALID_NUMBER:
        print(lower_bound, upper_bound)
        print(section)
        print(min(section) + max(section))
        break
