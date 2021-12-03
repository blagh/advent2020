instructions = []

with open("day02.txt") as file:
    instructions = [line.split(" ") for line in file.readlines()]

print(instructions)

depth = 0
dista = 0
for i in instructions:
    dir = i[0]
    qua = int(i[1])

    if dir == "forward":
        dista += qua
    elif dir == "down":
        depth += qua
    elif dir == "up":
        depth -= qua

    print(dir, qua, dista, depth)

print(dista, depth, dista*depth)

aim = 0
depth = 0
posit = 0
dista = 0
depth = 0

for i in instructions:
    dir = i[0]
    qua = int(i[1])

    if dir == "forward":
        dista += qua
        depth += aim * qua
    elif dir == "down":
        aim += qua
    elif dir == "up":
        aim -= qua

    print(dir, qua, aim, ":", dista, depth)

print(dista, depth, dista*depth)
