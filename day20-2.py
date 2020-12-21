from collections import defaultdict
from functools import reduce

def rotate(lines):
    return ["".join(list(l)) for l in zip(*lines[::-1])]

def flip(lines):
    return [l[::-1] for l in lines]

class Tile:
    def __init__(self, lines):
        self.id = int(lines[0][-5:-1])
        self.lines = lines[1:]
        self._extract_borders(lines[1:])
        self.is_edge = False
        self.top = None
        self.left = None
        self.right = None
        self.bottom = None

    def _extract_borders(self, lines):
        self.top_border = lines[0]
        self.bottom_border = lines[-1]
        self.left_border = "".join([l[0] for l in lines])
        self.right_border = "".join([l[-1] for l in lines])
        self.borders = [self.top_border, self.bottom_border, self.left_border, self.right_border]

    def set_border(self, border, tile):
        reverse = border[::-1]

        if self.top_border == border or self.top_border == reverse:
            self.top = tile
        elif self.left_border == border or self.left_border == reverse:
            self.left = tile
        elif self.right_border == border or self.right_border == reverse:
            self.right = tile
        elif self.bottom_border == border or self.bottom_border == reverse:
            self.bottom = tile

        self.border_tiles = [self.top, self.right, self.bottom, self.left]


    def rotate(self):
        self.lines = rotate(self.lines)

        temp = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = temp
        self.border_tiles = [self.top, self.right, self.bottom, self.left]

        self._extract_borders(self.lines)


    def flip(self):
        self.lines = self.lines[::-1]

        (self.top, self.bottom) = (self.bottom, self.top)
        self.border_tiles = [self.top, self.right, self.bottom, self.left]

        self._extract_borders(self.lines)

    def flap(self):
        self.lines = [l[::-1] for l in self.lines]
        (self.right, self.left) = (self.left, self.right)
        self.border_tiles = [self.top, self.right, self.bottom, self.left]

        self._extract_borders(self.lines)

    def __repr__(self):
        return str(self.id) + "\n" + "\n".join(self.lines)


tiles = []
with open("day20input.txt") as file:
    block = []
    for l in file.readlines():
        l = l[:-1]
        if not l:
            tiles += [Tile(block)]
            block = []
        else:
            block += [l]

tiles += [Tile(block)]

borders = defaultdict(list)
for tile in tiles:
    for b in tile.borders:
        reverse = b[::-1]
        if reverse in borders:
            borders[reverse].append(tile)
        else:
            borders[b].append(tile)

edges = []
for b in borders:
    if len(borders[b]) == 1:
        borders[b][0].is_edge == True
        edges += borders[b]

corners = []
for e in edges:
    if edges.count(e) == 2 and e not in corners:
        corners.append(e)

# build tile mesh
for border in borders:
    tiles = borders[border]
    if len(tiles) == 1:
        continue

    first_tile = tiles[0]
    second_tile = tiles[1]
    first_tile.set_border(border, second_tile)
    second_tile.set_border(border, first_tile)

TILE_WIDTH = 10

def add_to_map(map, tile, off_x, off_y):
    off_x = off_x * TILE_WIDTH
    off_y = off_y * TILE_WIDTH

    for y in range(TILE_WIDTH):
        line = tile.lines[y]
        for x in range(TILE_WIDTH):
            thing = line[x]
            map[off_y + y][off_x + x] = thing


def print_map(map):
    print("\n\n ~~~ full map ~~~ ")
    max_y = max(map.keys()) + 1
    for y in range(max_y):
        line = map[y]
        line_str = ""
        max_x = max(line.keys()) + 1
        for x in range(max_x):
            if (x % TILE_WIDTH and y % TILE_WIDTH):
                line_str += line[x]
            else:
                line_str += "*" if line[x] == "#" else " "

        print(line_str)

# print("corners", corners)

# pick a corner
tile = corners[0]
print("\nrotating ~~")
while tile.left is not None or tile.top is not None:
    tile.rotate()
    # print(tile.left.id if tile.left else None, tile.top.id if tile.top else None, tile)

# print([t.id if t else None for t in tile.border_tiles], tile)
complete_map = defaultdict(lambda: defaultdict(lambda: "`"))

x = 0
y = 0
while tile.bottom:
    first_tile = tile
    while tile.right:
        add_to_map(complete_map, tile, x, y)
        print_map(complete_map)

        while tile != tile.right.left:
            print("\n", tile.id, tile.right.left.id if tile.right.left else "None")
            print("rotating ~~~", tile.right)
            tile.right.rotate()

        if tile.right_border != tile.right.left_border:
            print(tile.right_border, tile.right.left_border)
            print("flipping ~~~", tile.right)
            tile.right.flip()

        print(tile.id, tile.right.left.id)
        print("look at this right ~~~", tile.right)
        tile = tile.right
        x += 1

    while first_tile != first_tile.bottom.top:
        print("\n", first_tile.id, first_tile.bottom.left.id if first_tile.bottom.left else "None")
        print("rotating ~~~", first_tile.bottom)
        first_tile.bottom.rotate()

    if first_tile.bottom_border != first_tile.bottom.top_border:
        print(first_tile.bottom_border, first_tile.bottom.top_border)
        print("flapping ~~~", first_tile.bottom)
        first_tile.bottom.flap()

    print("look at this bottom ~~~", first_tile.bottom)
    tile = first_tile.bottom
    x = 0
    y += 1

print_map(complete_map)
