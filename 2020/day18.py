
def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def math_it(expression, i=0, depth=0):
    if i == 0:
        print(expression)

    result = None
    operator = None
    while i < len(expression):
        e = expression[i]
        if e == " ":
            pass

        elif e == "(":
            print(" " * depth + "-->")
            (sub_result, i) = math_it(expression, i+1, depth+3)
            if result == None:
                print(" " * depth + f"{sub_result}")
                result = sub_result
            else:
                print(" " * depth + f" {operator.__name__} {result}")
                result = operator(result, sub_result)
                operator = None
                print(" " * depth + f"{result}")
        elif e == ")":
            return result, i

        elif e == "+":
            operator = add
        elif e == "*":
            operator = mult
        elif e.isnumeric():
            num = int(e)
            if result == None:
                print(" " * depth + f"{num}")
                result = num
            else:
                print(" " * depth + f" {operator.__name__} {num}")
                result = operator(result, num)
                operator = None
                print(" " * depth + f"{result}")

        i += 1

    return result, i

expressions = [
    ["1 + 2 * 3 + 4 * 5 + 6", 71],
    ["1 + (2 * 3) + (4 * (5 + 6))", 51],
    ["2 * 3 + (4 * 5)", 26],
    ["5 + (8 * 3 + 9 + 3 * 4 * 3)", 437],
    ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240],
    ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632],
    ["5 + (9 + (7 + 5 + 3 * 8 + 4 * 6) + 9 * 8 * 7)", 42677],
    ["7 * 4", 28],
    ["8", 8],
    ["(((1 + 2) + 3) + 4) + 5", 15],
    ["(1 + (2 + (3 + (4 + 5))))", 15],
    ["1 * ((2 + 3) + 4) + ((5))", 14],
    ["((5 + 4)) * 2 + 1", 19],
]

for case, expected in expressions:
    (actual, i) = math_it(case)
    if actual != expected:
        print(f"NFG {case}: {expected}, {actual}\n")
    else:
        print(f"WOOO {case}: {expected}\n")

total = 0
with open("day18input.txt") as file:
    lines = [math_it(l)[0] for l in file.readlines()]
    for line in lines:
        total += line
    print(total)
