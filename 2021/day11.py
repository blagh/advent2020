class Octo:
    def __init__(self, value):
        self.value = int(value)
        self.flashed = False

    def incr(self):
        self.value += 1

    def _should_flash(self):
        return self.value > 9 and not self.flashed

    def flash(self):
        if not self._should_flash():
            return False

        self.flashed = True
        return True

    def reset(self):
        self.flashed = False
        if self.value > 9:
            self.value = 0

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)

def print_grid(grid):
    print("\n".join("".join(str(m)) for m in grid), "\n----\n")

def apply_to_neighbours(method, grid, i, j):
    apply_this(method, grid, i, j+1)
    apply_this(method, grid, i, j-1)

    apply_this(method, grid, i+1, j+1)
    apply_this(method, grid, i+1, j-1)
    apply_this(method, grid, i+1, j)

    apply_this(method, grid, i-1, j+1)
    apply_this(method, grid, i-1, j-1)
    apply_this(method, grid, i-1, j)

def apply_this(method, grid, i, j):
    if i >= GRID_SIZE or i < 0 or j >= GRID_SIZE or j < 0:
        return

    method(grid, i, j)

def increment(octos, i, j):
    octos[i][j].incr()

def flash_tick(octos):
    new_flash = False

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            flashed = octos[i][j].flash()

            if flashed:
                apply_to_neighbours(increment, octos, i, j)
                new_flash = True

    return new_flash

def tick(octos):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            octos[i][j].incr()

    keep_flashing = True
    while keep_flashing:
        keep_flashing = flash_tick(octos)

    flashes = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if octos[i][j].flashed:
                flashes += 1
                octos[i][j].reset()

    return flashes

def sum_all(octos):
    s = 0
    for line in octos:
        for o in line:
            s += o.value
    return s

octopuses = []

with open("day11.txt") as file:
    octopuses = [line[:-1] for line in file.readlines()]
    octopuses = [[Octo(o) for o in line] for line in octopuses]

GRID_SIZE = len(octopuses)
TICKS = 200

i = 0
flashes = 0
print_grid(octopuses)
while True:
    i += 1
    print("*** TICK", i, "***")

    flashes += tick(octopuses)
    print_grid(octopuses)
    if sum_all(octopuses) == 0:
        break

print(flashes)
