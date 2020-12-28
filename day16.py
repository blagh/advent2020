from collections import defaultdict

fields = {}
with open("day16fields.txt") as file:
    lines = file.readlines()
    for line in lines:
        tokens = line.split(": ")
        field_name = tokens[0]
        ranges = tokens[1].split(" or ")

        fields[field_name] = [[int(x) for x in r.split("-")] for r in ranges]

print(fields)

your_ticket = [7, 1, 14]

nearby_tickets = []
with open("day16input.txt") as file:
    lines = file.readlines()
    nearby_tickets = [[int(x) for x in l[:-1].split(",")] for l in lines]

print(nearby_tickets)

invalid_values = []
valid_tickets = []
for ticket in nearby_tickets:
    valid_ticket = True
    for value in ticket:
        in_range = False

        for ranges in fields.values():
            for r in ranges:
                raange = range(r[0], r[1] + 1)
                if value in raange:
                    in_range = True

        if not in_range:
            print(value, raange)
            invalid_values.append(value)
            valid_ticket = False

    if valid_ticket:
        valid_tickets.append(ticket)


print(sum(invalid_values))

for t in valid_tickets:
    print(t)

field_positions = defaultdict(set)
non_positions = defaultdict(set)
for t in valid_tickets:
    for i in range(len(t)):
        value = t[i]

        for field in fields:
            in_range = False
            ranges = fields[field]
            for r in ranges:
                raange = range(r[0], r[1] + 1)
                if value in raange:
                    in_range = True

            print(field, value, in_range, ranges)
            if in_range and i not in non_positions[field]:
                field_positions[field].add(i)
            else:
                if i in field_positions[field]:
                    print("removing!")
                    field_positions[field].remove(i)
                non_positions[field].add(i)
            print(field_positions[field], non_positions[field])

print("")
for f in field_positions:
    print(f"{f}: {field_positions[f]}")

made_a_change = True
while made_a_change:
    made_a_change = False
    for field in field_positions:
        if len(field_positions[field]) == 1:
            index = list(field_positions[field])[0]
            for other_field in field_positions:
                if field != other_field and index in field_positions[other_field]:
                    field_positions[other_field].remove(index)
                    made_a_change = True

print("")
for f in field_positions:
    print(f"{f}: {field_positions[f]}")
