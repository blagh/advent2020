numbers = []

with open("day1input.txt") as file:
    numbers = [int(line) for line in file.readlines()]

print(numbers)

for x in numbers:
    for y in numbers:
        for z in numbers:
            if x + y + z == 2020:
                print(x, y, z, x*y*z)
