numbers = []

with open("day01.txt") as file:
    numbers = [int(line) for line in file.readlines()]

print(numbers)

prev_x = 141
inc_count = 0
for x in numbers:
    if x > prev_x:
        inc_count += 1
    prev_x = x

print(inc_count)
