from collections import defaultdict

template = ""
inserts = {}

with open("day14.txt") as file:
    lines = file.readlines()
    template = lines[0][:-1]

    for line in lines[2:]:
        pair, insert = line[:-1].split(" -> ")
        first_new_pair = pair[0] + insert
        second_new_pair = insert + pair[1]

        inserts[pair] = [insert, first_new_pair, second_new_pair]
# part 1
def step(template, inserts):
    new_template = template[0]
    prev_char = template[0]

    offset = 0
    for this_char in template[1:]:
        pair = prev_char + this_char

        if pair in inserts:
            new_template += inserts[pair][0]

        new_template += this_char
        prev_char = this_char

        print(new_template)

    return new_template

def count_pairs(template):
    char_counts = defaultdict(int)
    pair_counts = defaultdict(int)

    prev_char = template[0]
    char_counts[prev_char] += 1

    for this_char in template[1:]:
        pair = prev_char + this_char
        pair_counts[pair] += 1
        char_counts[this_char] += 1

        prev_char = this_char

    return char_counts, pair_counts

# part 2
char_counts, pair_counts = count_pairs(template)

def pair_step(pair_counts, char_counts, inserts):
    keys = list(pair_counts.keys())
    new_pair_counts = defaultdict(int)

    for p in keys:
        if p in inserts and pair_counts[p] > 0:
            new_char, first_new_pair, second_new_pair = inserts[p]

            new_pair_counts[first_new_pair] += pair_counts[p]
            new_pair_counts[second_new_pair] += pair_counts[p]

            char_counts[new_char] += pair_counts[p]
            # print("   ", p, " -> ", new_char, "|", first_new_pair, second_new_pair)

    return new_pair_counts

steps = 40
print('template', template, "\npairs", pair_counts, "\nchars", char_counts, "\n")

for i in range(steps):
    # template = step(template, inserts)
    # t_chars, t_pairs = count_pairs(template)

    pair_counts = pair_step(pair_counts, char_counts, inserts)
    # print('step', i + 1, "\ntemplate", template, "\npairs", pair_counts, "\ntairs", t_pairs, "\nchars", char_counts, "\n", 'step', i + 1, sum(char_counts.values()), len(template), "\n")
    print('step', i + 1, "\npairs", pair_counts, "\nchars", char_counts, "\n", 'step', i + 1, sum(char_counts.values()), "\n")


min_char = template[0]
max_char = template[0]
min_value = char_counts[min_char]
max_value = char_counts[max_char]

for b in char_counts.keys():
    if char_counts[b] > max_value:
        max_value = char_counts[b]
        max_char = b

    if char_counts[b] < min_value:
        min_value = char_counts[b]
        min_char = b

print("max", max_value, max_char)
print("min", min_value, min_char)
print(max_value - min_value)
