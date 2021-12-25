lines = []

openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]
points = [3, 57, 1197, 25137]

with open("day10.txt") as file:
    lines = [o[:-1] for o in file.readlines()]

score = 0
leftovers = []
for line in lines:
    stack = []
    corrupted = False
    for char in line:
        if char in openers:
            stack.append(char)
            continue

        if not stack:
            corrupted = True
            continue

        closer_x = closers.index(char)
        opener_x = openers.index(stack.pop())

        if closer_x != opener_x:
            corrupted = True
            print(line, "Expected", closers[opener_x], "found", char)
            score += points[closer_x]

    if stack and not corrupted:
        leftovers.append(stack)

print(score)
print(leftovers)

scores = []
for left in leftovers:
    score = 0
    completion = ""
    for char in left:
        opener_x = openers.index(char)
        completion += closers[opener_x]

    completion = completion[::-1]
    for char in completion:
        pre_score = score

        closer_x = closers.index(char)
        score = score * 5 + closer_x + 1
        print("  ", pre_score, pre_score * 5, closer_x + 1, score)

    print("Complete by adding", completion, score)
    scores.append(score)

scores.sort()
middle_x = int(len(scores) / 2)
print(scores, len(scores), middle_x)

print(scores[middle_x])
