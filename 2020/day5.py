seats = []

def parse_binary(number, zero, one, max):
    print(number)
    min_number = 0
    max_number = max
    print(" ", min_number, max_number)
    for n in number:
        diff = max_number - min_number
        if n == zero:
            if diff <= 2:
                print(zero, min_number)
                return min_number
            max_number = int(max_number - diff / 2)
        elif n == one:
            if diff <= 2:
                print(one, min_number + 1)
                return min_number + 1
            min_number = int(min_number + diff / 2)

        print(zero if n == zero else one, min_number, max_number, "(" + str(diff) + ")")

with open("day5input.txt") as file:
    boards = file.readlines()
    for board in boards:
        board = board[:-1] ## strip newline

        # do row
        row = parse_binary(board[:7], "F", "B", 128)
        # do column
        col = parse_binary(board[7:], "L", "R", 8)

        print(row, col, row * 8 + col)
        seats.append(row * 8 + col)

srted = sorted(seats)
print(srted)
i = 1

while (i < len(srted)):
    diff = srted[i - 1] - srted[i]
    print(srted[i-1], srted[i], diff)
    if (diff == -2):
        print(srted[i])
        break
    i += 1


print(max(seats))
