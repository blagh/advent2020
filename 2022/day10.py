def run_test(input, expected, test_method):
    actual = test_method(input)

    print(input, "\nactual:", actual, "\nexpect:", expected)
    assert(expected == actual)

def run_tests(tests, test_method):
    for input, expected in tests:
        run_test(input, expected, test_method)


def print_screen(screen):
    scr_str = ""

    for i, s in enumerate(screen):
        scr_str += s
        if (i+1) % 40 == 0:
            scr_str += "\n"

    print("screen")
    print(scr_str)
    print("-" * 40)

cycle = 1
strength = 0
x = 1
screen = []

def tick():
    global cycle, strength, x, screen

    mod_40 = (cycle-1) % 40
    print(cycle, ":", mod_40-1, x, mod_40+1)
    if x >= mod_40-1 and x <= mod_40+1:
        draw = "#"
    else:
        draw = "."

    screen.append(draw)
    print_screen(screen)

    cycle += 1

    # if cycle == 20 or ((cycle - 20) % 40 == 0) and cycle <= 220:
    #     strength += cycle * x
        # print("~~~interest!", cycle, x, cycle * x, strength)
        


def process(instruction):
    global cycle, strength, x

    tokens = [i.strip() for i in instruction.split(" ")]

    if tokens[0] == "noop":
        tick()

    elif tokens[0] == "addx":
        tick()
        tick()

        to_add = int(tokens[1])
        x += to_add

with open('day10test.txt') as file:
    for instruction in file.readlines():
        process(instruction)

# print(strength)
print_screen(screen)

cycle = 1
strength = 0
x = 1
screen = []

with open("day10input.txt") as file:
    for instruction in file.readlines():
        process(instruction)

print(strength)
print_screen(screen)