from collections import defaultdict
from functools import reduce

def run_test(input, expected, test_method):
    actual = test_method(input)

    print(input, "\nactual:", actual, "\nexpect:", expected)
    assert(expected == actual)

def run_tests(tests, test_method):
    for input, expected in tests:
        run_test(input, expected, test_method)

def print_2d_array(array):
    print("\n".join(["".join(line) for line in array]), "\n\n\n")

def print_2d_defaultdict(d, snake):
    input_string = ""

    min_x = max_x = min_y = max_y = 0
    for x in d.keys():
        if x > max_x: max_x = x
        if x < min_x: min_x = x
        for y in d[x].keys():
            if y > max_y: max_y = y
            if y < min_y: min_y = y

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if d[x][y] == "x":
                input_string += d[x][y]
            elif ([x,y] in snake):
                input_string += str(snake.index([x,y]))
            else:
                input_string += d[x][y]
        input_string += "\n"

    print(input_string + "-" * 184 + "\n")

def tick(snake, x_diff, y_diff):
    old_head = snake[0]
    snake[0] = [snake[0][0] + x_diff, snake[0][1] + y_diff]

    for i in range(1, len(snake)):
        #print(snake[i-1], snake[i], x_diff, y_diff)

        new_tail = tick_tail(snake[i-1], snake[i][:], x_diff, y_diff)

        # print(new_tail)
        if new_tail == snake[i]:
            #input("wait ... ")
            break

        old_head = snake[i]
        snake[i] = new_tail

        #print(snake)
        #input("wait ... ")

    return snake

def tick_tail(head, tail, x_diff, y_diff):
    # tail doesn't need to move, head is on top or right next already
    if head == tail or abs(head[1] - tail[1]) <= 1 and abs(head[0] - tail[0]) <= 1:
        # print('no move', abs(head[1] - tail[1]), abs(head[0] - tail[0]))
        return tail

    # tail needs to move diagonally
    # print('~ shift it ~')
    if head[0] > tail[0]:
        tail[0] += 1

    if head[1] > tail[1]:
        tail[1] += 1

    if head[0] < tail[0]:
        tail[0] -= 1

    if head[1] < tail[1]:
        tail[1] -= 1

    return tail

DIRECTIONS = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}
def move(snake, visited, direction, amount):
    (x_diff, y_diff) = DIRECTIONS[direction]

    for a in range(int(amount)):
        print(snake)
        print(direction, amount)

        snake = tick(snake, x_diff, y_diff)

        visited[snake[-1][0]][snake[-1][1]] = "x"

        for s in snake:
            if visited[s[0]][s[1]] != "x":
                visited[s[0]][s[1]] = "."

        print_2d_defaultdict(visited, snake)
        # input("wait ... ")

    return (snake, visited)

def run_moves(moves):
    visited = defaultdict(lambda: defaultdict(lambda: "."))
    snake = [[0,0] for i in range(10)]

    for (direction, amount) in moves:
        (snake, visited) = move(snake, visited, direction, amount)

    return sum(len(list(filter(lambda v: v == "x", line.values()))) for line in visited.values())

with open("day09input.txt") as file:
    map = [line.split(" ") for line in file.readlines()]

test_input = [
    ['R', '4'],
    ['U', '4'],
    ['L', '3'],
    ['D', '1'],
    ['R', '4'],
    ['D', '1'],
    ['L', '5'],
    ['R', '2']
]

test_input_2 = [
    ['R', '5'],
    ['U', '8'],
    ['L', '8'],
    ['D', '3'],
    ['R', '17'],
    ['D', '10'],
    ['L', '25'],
    ['U', '20']
]

run_test(test_input, 1, run_moves)
run_test(test_input_2, 36, run_moves)

print(run_moves(map))
