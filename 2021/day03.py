lines = []

with open("day03.txt") as file:
    lines = file.readlines()

print(lines)

gamma_rate = ""
epsil_rate = ""

total_lines = len(lines)
one_count = [0] * (len(lines[0]) - 1)

for l in lines:
    for i in range(len(l) - 1):
        if l[i] == "1":
            one_count[i] += 1

for i in range(len(one_count)):
    if one_count[i] > total_lines / 2:
        gamma_rate += "1"
        epsil_rate += "0"
    else:
        gamma_rate += "0"
        epsil_rate += "1"

print(gamma_rate, epsil_rate)

gamma_rate = int(str(gamma_rate), base=2)
epsil_rate = int(str(epsil_rate), base=2)

print(gamma_rate, epsil_rate)
print(gamma_rate * epsil_rate)
