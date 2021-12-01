from collections import defaultdict

whole_thing = ""

allergen_counts = defaultdict(int)

possible_allergens = defaultdict(lambda: defaultdict(int))
possible_ingrs = defaultdict(lambda: defaultdict(int))
# foods = []
#
# class Food:
#     def __init__(self, ingrs, allrs):
#         self.ingrs = ingrs
#         self.allrs = allrs

with open("day21input.txt") as file:
    for food in file.readlines():
        whole_thing += food
        tokens = food.split("(")
        ingredients = tokens[0][:-1].split(" ")
        allergens = tokens[1][9:-2].split(", ")

        # food = Food(ingredients, allergens)

        for i in ingredients:
            for a in allergens:
                possible_ingrs[i][a] += 1

        for a in allergens:
            allergen_counts[a] += 1
            for i in ingredients:
                possible_allergens[a][i] += 1


print(possible_allergens)
print(possible_ingrs)

made_a_change = True
while made_a_change:
    made_a_change = False
    for food in possible_ingrs:
        # ugliest thing ever, sort the dictionary by items in reverse order
        allergens = {k: v for k, v in reversed(sorted(possible_ingrs[food].items(), key=lambda item: item[1]))}

        for allergen in allergens:
            print(food, allergen, allergens[allergen], allergen_counts[allergen])

            # pick the first matching allergen
            if allergens[allergen] == allergen_counts[allergen]:
                for other_food in possible_ingrs:
                    if food != other_food and allergen in possible_ingrs[other_food]:

                        del possible_ingrs[other_food][allergen]
                        made_a_change = True

                for other_allergen in allergens:
                    print(allergen, other_allergen, possible_ingrs[food])
                    if allergen != other_allergen and other_allergen in possible_ingrs[food]:

                        del possible_ingrs[food][other_allergen]
                        made_a_change = True

                if made_a_change:
                    print(food, possible_ingrs[food])
                    break

print("")
for food in possible_ingrs:
    print(f"{food}: {possible_ingrs[food]}")

print("\ncounts:", allergen_counts)

no_allergen = []
for food in possible_ingrs:
    if not possible_ingrs[food]:
        no_allergen.append(food)

print(no_allergen)
print(whole_thing)
print([(no_a, whole_thing.count(no_a)) for no_a in no_allergen])
print(sum(whole_thing.count(no_a) for no_a in no_allergen))
