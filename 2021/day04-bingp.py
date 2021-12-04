import itertools

lines = []

class Board:
    _false = "."
    _true = "*"

    def __init__(self, lines):
        self.lines = [l.split() for l in lines]
        # lolsob can't do `[[self._false] * 5] * 5`
        # cause each row ends up having the same reference
        self.marked = [[self._false] * 5 for i in range(5)]

    def mark(self, number):
        # using itertools so we don't need to break out of nested loops
        for i, j in itertools.product(range(5), range(5)):
            if self.lines[i][j] == number:
                self.marked[i][j] = self._true
                break

    def unmarked_square_sum(self):
        sum = 0
        for i, j in itertools.product(range(5), range(5)):
            if self.marked[i][j] == self._false:
                sum += int(self.lines[i][j])

        return sum

    def check_victory(self):
        for i in range(5):
            empty_col_found = False
            empty_row_found = False
            for j in range(5):
                if self.marked[i][j] == self._false:
                    empty_col_found = True

                if self.marked[j][i] == self._false:
                    empty_row_found = True

            if not empty_col_found:
                return True

            if not empty_row_found:
                return True

    def __str__(self):
        return ("------\n" + "\n".join([" ".join(l) for l in self.lines]) + "\n" +
                "------\n" + "\n".join([" ".join(l) for l in self.marked]) + "\n" )

    def __repr__(self):
        return ("------\n" + "\n".join([" ".join(l) for l in self.lines]) + "\n" +
                "------\n" + "\n".join([" ".join(l) for l in self.marked]) + "\n" )

with open("day04.txt") as file:
    lines = file.readlines()

numbers = lines[0].split(",")

boards = []
for i in range(2, len(lines), 6):
    boards.append(Board(lines[i:i+5]))

print(numbers)
print("\n\n\nhere we go ~~~\n\n\n")

for n in numbers:
    if len(boards) == 0:
        break

    print("checking for", n, "\n\n")
    print("boards left:", len(boards))

    for b in boards[:]:
        b.mark(n)

        if b.check_victory():
            print("board is done, last number", n)
            print(b)

            unmarked_sum = b.unmarked_square_sum()
            print("unmarked squares", unmarked_sum)
            print("score:", unmarked_sum * int(n))

            boards.remove(b)
