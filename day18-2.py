class Node:
    def __init__(self, value):
        self.value = value
        if callable(self.value):
            self.left = None
            self.right = None

    def add_child(self, child):
        # print(f"adding child: {child}")

        if not callable(self.value):
            # print(f"{self.value} not callable -- returning")
            return False

        if not self.left:
            # print(f"adding as left node")
            self.left = child
            return True

        if not self.right:
            # print(f"adding as right node")
            self.right = child
            return True

        if callable(child.value):
            # print(f"pushing in an operation")
            child.add_child(self.right)
            self.right = child

            return True

        if self.left.add_child(child):
            return True
            # print(f"recursive left add success")

        if self.right.add_child(child):
            return True
            # print(f"recursive right add success")

        return False

    def apply(self):
        if self.value == BRACKET:
            left = self.left.apply()
            # print(f"{self.value}: {left}")

            return left

        if callable(self.value):
            left = self.left.apply()
            right = self.right.apply()
            # print(f"{self.value.__name__}: {left} {right}")

            return self.value(left, right)

        return self.value

    def __repr__(self):
        if self.value == BRACKET:
            return f"({self.left})"

        if callable(self.value):
            if self.value == add:
                return f"({self.left} {self.value.__name__} {self.right})"
            return f"{self.left} {self.value.__name__} {self.right}"

        return f"n{self.value}"

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

TAB = "  "
BRACKET = "()"

def parse_it(expression, i=0, depth=0):
    if i == 0:
        print(expression)

    root = None

    while i < len(expression):
        if expression[i] != " ":
            print(TAB * depth + f"[{i}: {expression[i]}]")

        e = expression[i]
        if e == " ":
            pass
        elif e == ")":
            return root, i
        elif e == "(":
            node = Node("()")

            sub_root, i = parse_it(expression, i+1, depth+1)
            node.left = sub_root

            print(sub_root, node, root)
            if root == None:
                root = node
            else:
                root.add_child(node)

        elif e == "+":
            node = Node(add)
            if not root.add_child(node):
                node.left = root
                root = node

        elif e == "*":
            node = Node(mult)
            node.left = root
            root = node

        elif e.isnumeric():
            node = Node(int(e))
            if root == None:
                root = node
            else:
                root.add_child(node)

        if expression[i] != " ":
            print(TAB * depth, root)
        i += 1

    return root

def math_it(expression):
    tree = parse_it(expression)
    return tree.apply()

expressions = [
    ["1 + 2 * 3 + 4 * 5 + 6", 231],
    ["2 * 3 + (4 * 5)", 46],
    ["1 + (2 * 3) + (4 * (5 + 6))", 51],
    ["5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445],
    ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060],
    ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340],
    ["7 * 4", 28],
    ["8", 8],
    ["(((1 + 2) + 3) + 4) + 5", 15],
    ["(1 + (2 + (3 + (4 + 5))))", 15],
    ["1 * ((2 + 3) + 4) + ((5))", 14],
    ["((5 + 4)) * 2 + 1", 27],
    ["1 + 2 * (3 + 4) + 5", (1+2)*((3+4)+5)],
    ["1 * 2 * 3 * 4 * 5", 1*2*3*4*5],
    ["1 + 2 * 3 + 4 * 5", (1+2)*(3+4)*5],
    ["8 * (7 * 9 * 5) * 4 + 5", 8*(7*9*5)*(4+5)],
    ["3 * ((7 * 8 + 5 * 7) + 6) * 4 + 8 + 3", 3 * ((7*(8+5)*7)+6) * (4+8+3)],
]

for case, expected in expressions:
    actual = math_it(case)
    if actual != expected:
        print(f"NFG {case}: {expected}, {actual}\n")
        break
    else:
        print(f"WOOO {case}: {expected}\n")

total = 0
with open("day18input.txt") as file:
    lines = [math_it(l) for l in file.readlines()]
    for line in lines:
        total += line
    print(total)
