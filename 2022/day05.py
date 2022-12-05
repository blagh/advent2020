from collections import defaultdict

stacks = defaultdict(list)

def make_move(stacks, count, col_a, col_b):
    for c in range(count):
        box = stacks[col_a].pop()
        stacks[col_b].append(box)

def make_move_2(stacks, count, col_a, col_b):
    boxes = stacks[col_a][-count:]

    stacks[col_b].extend(boxes)
    stacks[col_a] = stacks[col_a][:-count]

making_stacks = True
with open("day05input.txt") as file:
    for line in file.readlines():

        if making_stacks:
            if not line.strip():
                print("done with stacks")
                print(stacks)
                making_stacks = False
                continue

            for i in range(0, len(line), 4):
                chunk = line[i:i+4].strip()

                if not chunk:
                    continue
                
                stacks[int(i/4) + 1].insert(0, chunk)

        else:
            # move 1 from 2 to 1
            line = line.strip("move ")
            _move, _from = line.split(" from ")
            col_a, col_b = _from.split(" to ")

            _move = int(_move)
            col_a = int(col_a)
            col_b = int(col_b)

            print(line)

            make_move_2(stacks, _move, col_a, col_b)

            print(stacks)

stack_string = ""
for i in range(1, len(stacks)+1):
    stack_string += stacks[i].pop()[1]

print(stack_string)