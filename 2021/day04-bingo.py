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
        for i, j in itertools.product(range(5), range(5)):
            if self.lines[i][j] == number:
                self.marked[i][j] = self._true
                print("found", i, j, "\n", self)
                break

    def unmarked_square_sum(self):
        sum = 0
        for i, j in itertools.product(range(5), range(5)):
            if self.marked[i][j] == self._false:
                print("summing", self.lines[i][j])
                sum += int(self.lines[i][j])

        return sum

    def check_victory(self):
        for i in range(5):
            # check row i
            if not self._false in self.marked[i]:
                return True

            # check column i
            empty_row_found = False
            for j in range(5):
                if self.marked[j][i] == self._false:
                    empty_row_found = True

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
    print("checking for", n, "\n\n")

    for i in range(len(boards)):
        b = boards[i]
        b.mark(n)

        if b.check_victory():
            print("pick board", i+1, "last number", n)

            unmarked_sum = b.unmarked_square_sum()
            print("unmarked squares", unmarked_sum)
            print("answer:", unmarked_sum * int(n))

            break

    if b.check_victory():
        break
