from collections import defaultdict
from functools import reduce


class Tile:
    def __init__(self, lines):
        self.id = int(lines[0][-5:-1])
        self.borders = Tile._extract_borders(lines[1:])
        # self.border_count = 0
        # self.border_tiles = {b: None for b in borders}

    def _extract_borders(lines):
        # print(lines)
        top_border = lines[0]
        bottom_border = lines[-1]
        left_border = "".join([l[0] for l in lines])
        right_border = "".join([l[-1] for l in lines])
        return [top_border, bottom_border, left_border, right_border]

    # def __repr__(self):
    #     return f"{self.id}: " + '|'.join(self.borders)

    def __repr__(self):
        return str(self.id)

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

print(tiles)

borders = defaultdict(list)
for tile in tiles:
    for b in tile.borders:
        reverse = b[::-1]
        if reverse in borders:
            borders[reverse].append(tile)
        else:
            borders[b].append(tile)


    print(borders, "\n")

edges = []
for b in borders:
    if len(borders[b]) == 1:
        edges += borders[b]

corners = []
for e in edges:
    if edges.count(e) == 2 and e.id not in corners:
        corners.append(e.id)

print(list(corners))
print(reduce(lambda a,b: a*b, corners))
