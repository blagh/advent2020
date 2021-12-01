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

# prev_sum = 199 + 200 + 208
prev_sum = 141 + 152 + 164
inc_count = 0
for i in range(len(numbers)):

    new_sum = sum(numbers[i:i+3])

    print(prev_sum, numbers[i:i+3], new_sum)

    if new_sum > prev_sum:
        inc_count += 1
    prev_sum = new_sum

print(inc_count)
