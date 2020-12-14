valid_bags = {}

def clean_bag_name(name):
    tokens = name.split(" ")
    if tokens[0].isnumeric():
        return (int(tokens[0]), tokens[1] + tokens[2])
    return tokens[0] + tokens[1]

with open("day7input.txt") as file:
    lines = file.readlines()
    for line in lines:
        rule = line[:-2].split(" contain ")
        bag = clean_bag_name(rule[0])

        print(rule)
        innards = None
        if "," in rule[1]:
            innards = [clean_bag_name(r) for r in rule[1].split(", ")]
        elif rule[1] != "no other bags":
            innards = [clean_bag_name(rule[1])]
        valid_bags[bag] = innards

def count_children(this_bag, depth=0):
    print("--" * depth, this_bag)
    if not valid_bags.get(this_bag):
        return 1

    count = 0
    for (spread, child_bag) in valid_bags[this_bag]:
        child_count = count_children(child_bag, depth + 1)
        count += spread * child_count
        print("  " * depth, "+", spread, child_bag, child_count)

    print("--" * depth, count)
    return count + 1

count = 0
valid_bags

print(count_children("shinygold"))
