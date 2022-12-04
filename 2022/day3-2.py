from functools import reduce

sum = 0

def get_priority(char):
    ord_char = ord(char)

    ord_a = ord("a")
    ord_A = ord("A")

    if ord_char >= ord_a:
        priority = ord_char - ord_a + 1
    else:
        priority = ord_char - ord_A + 27

    return priority

with open("day3input.txt") as file:
    rucksacks = [line[:-1] for line in file.readlines()]

for index in range(0, len(rucksacks), 3):
    group = rucksacks[index:index+3]

    print(group)

    common_set = reduce(
        lambda acc, sack: acc.intersection(set(sack)), 
        group, set(group[0])
    )
    
    print(common_set)
    common_char = common_set.pop()

    print(common_char)

    priority = get_priority(common_char)

    print(priority)

    sum += priority

print(sum)




