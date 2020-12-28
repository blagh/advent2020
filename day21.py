from collections import defaultdict

whole_thing = ""

possible_allergens = defaultdict(lambda: defaultdict(int))
possible_foods = defaultdict(lambda: defaultdict(int))
with open("day21input.txt") as file:
    for line in file.readlines():
        whole_thing += line
        tokens = line.split("(")
        ingredients = tokens[0][:-1].split(" ")
        allergens = tokens[1][9:-2].split(", ")

        for i in ingredients:
            for a in allergens:
                possible_foods[i][a] += 1

        for a in allergens:
            for i in ingredients:
                possible_allergens[a][i] += 1


print(possible_allergens)
print(possible_foods)

made_a_change = True
while made_a_change:
    made_a_change = False
    for food in possible_foods:
        allergens = possible_foods[food]
        print(food, allergens)
        for possible_allergen in allergens:
            if allergens[possible_allergen] > 1:
                for other_food in possible_foods:
                    if food != other_food \
                        and possible_allergen in possible_foods[other_food] \
                        and possible_foods[other_food][possible_allergen] < allergens[possible_allergen]:

                        possible_foods[other_food][possible_allergen] -= allergens[possible_allergen]

                        if possible_foods[other_food][possible_allergen] <= 0:
                            del possible_foods[other_food][possible_allergen]

                        made_a_change = True

print("")
for food in possible_foods:
    print(f"{food}: {possible_foods[food]}")

no_allergen = []
for food in possible_foods:
    if not possible_foods[food]:
        no_allergen.append(food)

print(no_allergen)
print(sum(whole_thing.count(no_a) for no_a in no_allergen))
