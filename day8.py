lines = []
lines_hit = []


with open("day8input.txt") as file:
    lines = file.readlines()

lines = [l[:-1] for l in lines]

def run(lines):
    line_no = 0
    acc = 0
    while line_no not in lines_hit:
        if line_no > len(lines):
            print("success!")
            print(acc)
            return True

        line = lines[line_no]

        print(line_no, line)
        lines_hit.append(line_no)

        (instruct, value) = line.split(" ")
        value = int(value)

        if instruct == "nop":
            line_no += 1
        elif instruct == "acc":
            acc += value
            line_no += 1
        elif instruct == "jmp":
            line_no += value

    print(acc)
    return False

run(lines)
