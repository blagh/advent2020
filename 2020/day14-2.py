from collections import defaultdict
from math import pow

memory = defaultdict(int)
instructions = []
mask = ""

def apply_mask(value, mask):
    binary = list(f"{value:036b}")
    print("v:", f"{value:036b}")
    for i in range(len(mask)):
        if mask[i] != "0":
            binary[i] = mask[i]
    print("V:", "".join(binary))
    return "".join(binary)

with open("day14input.txt") as file:
    instructions = file.readlines()
    for line in instructions:
        if "mask" in line:
            # mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
            mask = line[7:-1]
            print("M:", mask)
        else:
            tokens = line.split(" = ")
            # mem[17610] = 1035852
            address = int(tokens[0][4:-1])
            value = int(tokens[1])
            address = apply_mask(address, mask)
            memory[address] = value

print(memory)
print("----")

final_memory = defaultdict(int)
for m in memory:
    if "X" not in m:
        final_memory[m] = memory[m]
    else:
        x_count = m.count("X")
        for x in range(int(pow(2, x_count))):
            m_list = list(m)

            format_str = "{x:0" + str(x_count) + "b}"
            x_bin = list(format_str.format(x=x))

            for i in range(len(x_bin)):
                next_x = m_list.index("X")
                m_list[next_x] = x_bin[i]

            # add to memory
            print("".join(m_list))
            final_memory["".join(m_list)] = memory[m]

print(final_memory)
print(sum(final_memory.values()))
