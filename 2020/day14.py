from collections import defaultdict

memory = defaultdict(int)
instructions = []
mask = ""

def apply_mask(value, mask):

    binary = list(f"{value:036b}")
    for i in range(len(mask)):
        if mask[i] != 'X':
            binary[i] = mask[i]
    return int("".join(binary), 2)

with open("day14input.txt") as file:
    instructions = file.readlines()
    for line in instructions:
        if "mask" in line:
            # mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
            mask = line[7:-1]
            print(mask)
        else:
            tokens = line.split(" = ")
            # mem[17610] = 1035852
            address = int(tokens[0][4:-1])
            value = int(tokens[1])
            value = apply_mask(value, mask)
            memory[address] = value

print(memory)
print(sum([m for m in memory.values()]))
