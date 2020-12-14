valid_bags = {}

def clean_bag_name(name):
    tokens = name.split(" ")
    if tokens[0].isnumeric():
        return tokens[1] + tokens[2]
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

def check_for_shiny(this_bag):
    if not valid_bags.get(this_bag):
        # print(f"it's the end for {this_bag}")
        return set()

    colours = set()
    if "shinygold" in valid_bags[this_bag]:
        # print(f"can put bag in {this_bag}")
        colours.add(this_bag)

    for child_bag in valid_bags[this_bag]:
        children = check_for_shiny(child_bag)
        if children:
            # print(f"and in the children {children}")
            colours.add(this_bag)
        colours.update(children)

    return colours

colours = set()
for bag in valid_bags:
    colours.update(check_for_shiny(bag))

print(len(colours))
