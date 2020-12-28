from collections import defaultdict

possible_allergens = defaultdict(lambda: defaultdict(int))
possible_foods = defaultdict(lambda: defaultdict(int))
with open("day21input.txt") as file:
    for line in file.readlines():
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
        for possible_allergen in allergens:
            if allergens[possible_allergen] > 1:
                for other_food in possible_foods:
                    if food != other_food and possible_allergen in possible_foods[other_food]:
                        del possible_foods[other_food][possible_allergen]
                        made_a_change = True

print("")
for food in possible_foods:
    print(f"{food}: {possible_foods[food]}")
