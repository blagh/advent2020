

sum = 0
with open("day03input.txt") as file:
    for rucksack in file.readlines():
        rucksack = rucksack[:-1]

        print(rucksack)
        
        halfsies = int(len(rucksack) / 2)

        comp_1 = rucksack[:halfsies]
        comp_2 = rucksack[halfsies:]

        print(comp_1)
        print(comp_2)

        common_char = set(comp_1).intersection(set(comp_2)).pop()

        print(common_char)

        ord_char = ord(common_char)

        ord_a = ord("a")
        ord_A = ord("A")

        if ord_char >= ord_a:
            priority = ord_char - ord_a + 1
        else:
            priority = ord_char - ord_A + 27

        print(priority)

        sum += priority

print(sum)