groups = []

with open("day6input.txt") as file:
    lines = file.readlines()
    group = set()
    new_group = True
    for line in lines:
        if (line == "\n"):
            groups.append(group)
            group = set()
            print("reset ~~")
            new_group = True
        else:
            answers = set([c for c in line[:-1]])
            if new_group:
                group.update(answers)
                new_group = False
            else:
                group = group.intersection(answers)
            print(group, answers)


groups.append(group)
print(groups)
print([len(x) for x in groups])

summ = sum([len(x) for x in groups])
print(summ)
