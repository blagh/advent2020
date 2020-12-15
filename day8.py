lines = []

with open("day8input.txt") as file:
    lines = file.readlines()

lines = [l[:-1] for l in lines]

def run(these_lines):
    lines_hit = []
    line_no = 0
    acc = 0
    while line_no not in lines_hit:
        if line_no >= len(these_lines):
            print("success!")
            print(acc)
            return True

        line = these_lines[line_no]

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

    print("failure.")
    print(acc)
    return False

for i in range(len(lines)):
    success = False
    line = lines[i]
    if "acc" not in line:

        new_line = ""
        if "jmp" in line:
            new_line = "nop" + line[3:]
        elif "nop" in line:
            new_line = "jmp" + line[3:]

        print("new: ", new_line)
        new_lines = lines[:i] + [new_line] + lines[i+1:]
        print(new_lines)

        success = run(new_lines)
        if success:
            print("OMG")
            break
