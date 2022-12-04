lines = []

with open("day01input.txt") as file:
    lines = file.readlines()

sums = []
current_sum = 0
for line in lines:
    try:
        calories = int(line)
        current_sum += calories
    except:
        sums.append(current_sum)
        current_sum = 0

sums.append(current_sum)

print(sums)
sorted_sums = sorted(sums, reverse=True)[0:3]
print(sorted_sums)
print(sum(sorted_sums))
