from collections import defaultdict
from dataclasses import dataclass

def run_test(input, expected, test_method):
    actual = test_method(input)

    print(input, "\nactual:", actual, "\nexpect:", expected)
    assert(expected == actual)

def print_map(d, path):
    input_string = ""

    min_x = min_y = 0
    max_x = len(d)
    max_y = len(d[0])

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if ([x,y] in path):
                input_string += "."
            else:
                input_string += d[x][y].label
        input_string += "\n"

    print(input_string + "-" * max_x + "\n")
    print(str_path(path))

MAX_COST = 1_000_000_000

small_map = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split("\n")

big_map = """abcccccccccccccccccccccccccccccccaaaaaaaaaaaaaaaaccaaaaaaaaccccccccccccccccccccccccccccccccccccaaaaaa
abcccccccccccccccccccccccccccccccaaaaaaaaaaaaaaaaaccaaaaaaccccccccccccccccccccccccccccccccccccccaaaaa
abcccccccccccccccccccccccccccccccccaaaaaaaacccaaaaccaaaaaaccccccccccccccccccccaaaccccccccccccccccaaaa
abcccccccccccccccccccccccccccccccccccaaaaaaaccaaccccaaaaaaccccccccccccccccccccaaaccccccccccccccccaaaa
abcccccccccccccccccccccccccccccaaacccaaaaaaaacccccccaaccaaccccccccccccccccccccaaaccccccccccccccccaaac
abcccccccccccccccccccccccccccccaaaaaaaaacaaaacccccccccccccccaccaaccccccccccccciiaaccaaaccccccccccaacc
abccccccccaaccccccccccccccccccaaaaaaaaaaccaaacccccccccccccccaaaaaccccccccacaiiiiijjaaaacccccccccccccc
abacccaaccaacccccccccccccccccaaaaaaaaaaccccacccccaaaaccccccccaaaaacccccccaaiiiiijjjjaaaccccccaacccccc
abacccaaaaaacccccccccccccccccaaaaaaaaccccccccccccaaaacccccccaaaaaacccccccaiiiioojjjjjacccaaaaaacccccc
abcccccaaaaaaacccccccccccccccccaaaaaaccccaaccccccaaaacccccccaaaaccccccccciiinnoooojjjjcccaaaaaaaccccc
abccccccaaaaaccccccccccccccccccaaaaaacccaaaaccccccaaacccccccccaaaccccccchiinnnooooojjjjcccaaaaaaacccc
abcccccaaaaacccccccccccccccccccaacccccccaaaaccccccccccccccccccccccccccchhiinnnuuoooojjjjkcaaaaaaacccc
abccccaaacaaccccccccccccccccccccccccccccaaaaccccccccccccccccccaaacccchhhhhnnntuuuoooojjkkkkaaaacccccc
abccccccccaacccccccccccccccccccccccccccccccccccccccccccccccccccaacchhhhhhnnnnttuuuuoookkkkkkkaacccccc
abcccccccccccccccccccaacaaccccccccccccccccccccccccccccccccccaacaahhhhhhnnnnntttxuuuoopppppkkkkacccccc
abcccccccccccccccccccaaaaacccccccccaccccccccccccccccccccccccaaaaahhhhmnnnnntttxxxuuupppppppkkkccccccc
abccccccccccccccccccccaaaaacccccaaaacccccccccccccccccccccccccaaaghhhmmmmttttttxxxxuuuuuupppkkkccccccc
abcccccccccccccccccccaaaaaaaccccaaaaaaccccccccccccccccccccccccaagggmmmmtttttttxxxxuuuuuuvppkkkccccccc
abcccccccccccccccccccaaaaaaaaaaacaaaaacccccccccccccccccccccccaaagggmmmttttxxxxxxxyyyyyvvvppkkkccccccc
abccccccccccccccccccccaaaaaaaaaaaaaaaccccccccccccccccccccaacaaaagggmmmtttxxxxxxxyyyyyyvvppplllccccccc
SbcccccccccccccccccccaaaaaaaaaacaccaaccccccccccccccccccccaaaaaccgggmmmsssxxxxEzzzyyyyvvvpplllcccccccc
abcccccccccccccccccccccaaaaaaccccccccccccccaacaaccccccccaaaaaccccgggmmmsssxxxxyyyyyvvvvqqplllcccccccc
abccccccccccccccccccccccaaaaaacccccccccccccaaaacccccccccaaaaaacccgggmmmmsssswwyyyyyvvvqqqlllccccccccc
abcccccccccccccccccccccaaaaaaaccccccccccccaaaaacccccccccccaaaaccccgggmmmmsswwyyyyyyyvvqqllllccccccccc
abcccccccccccccccccccccaaaccaaacccccccccccaaaaaaccccccccccaccccccccgggooosswwwywwyyyvvqqlllcccccccccc
abccccccccccccccccccccccacccccccccccccccccacaaaacccccccccccccccccccfffooosswwwwwwwwvvvqqqllcccccccccc
abccccccccccccccccccccccccccccccccccccccccccaacccccccccccccccccccccfffooosswwwwwrwwvvvqqqllcccccccccc
abccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccffooossswwwrrrwvvvqqqmmcccccccccc
abccccaaacccccccccccccccccccccccccccccccccccccccccccccccccccccccccccffooosssrrrrrrrrqqqqmmmcccccccccc
abccccaaacaacccccaaccccaaaacccccccccccccccccccccccccccccccccccccccccffooossrrrrrnrrrqqqqmmmcccaaacccc
abcccccaaaaaccaaaaacccaaaaacccccccccccccccccccccccccccccccccccccccccfffoooorrnnnnnnmqqmmmmmcccaaacccc
abccaaaaaaaacccaaaaaccaaaaaaccccccccccccccccccccccccccccccccccccccccfffooonnnnnnnnnmmmmmmmcccaaaccccc
abcccaaaaacccccaaaaaccaaaaaaccccccaacccccccccccccccccccccccccccccccccfffoonnnnneddnmmmmmmccccaaaccccc
abccccaaaaacccaaaaacccaaaaaacccccaaaaaaccccccccccccccccccccaaccccccccffeeeeeeeeeddddddddccccaaaaccccc
abccccaacaaacccccaacccccaacccccccaaaaaaaccccccccccccccccaaaaaccccccccceeeeeeeeeedddddddddccaccaaccccc
abccccaacccccccccccccccccccccccccaaaaaaaccaaaccccccccccccaaaaaccccccccceeeeeeeeaaaaddddddcccccccccccc
abcccccccccccaaccccccccccccccccccccccaaaaaaaaacccccccccccaaaaacccccccccccccaaaacaaaacccccccccccccccaa
abccccccccaacaaacccccccccccccccccccccaaaaaaaacccccccccccaaaaaccccccccccccccaaaccaaaaccccccccccccccaaa
abccccccccaaaaacccccccccccccccccccccacaaaaaaccccccccccccccaaacccccccccccccccaccccaaacccccccccccacaaaa
abcccccccccaaaaaaccccccccccccccccaaaaaaaaaaacccccccccccccccccccccccccccccccccccccccacccccccccccaaaaaa
abcccccccaaaaaaaaccccccccccccccccaaaaaaaaaaaaacccccccccccccccccccccccccccccccccccccccccccccccccaaaaaa""".split("\n")

def estimate_cost(a_node, b_node):
    """h : also known as the heuristic value, it is the estimated cost of 
moving from the current cell to the final cell. The actual cost cannot be 
calculated until the final cell is reached. Hence, h is the estimated cost. 
We must make sure that there is never an over estimation of the cost."""

    # let's get euclidean
    x_diff = abs(a_node.x - b_node.y)
    y_diff = abs(a_node.y - b_node.y)

    prev_e = a_node.elevation
    cur_e = b_node.elevation
    z_diff = abs(prev_e - cur_e)

    print(x_diff, y_diff, z_diff, (x_diff^2 + y_diff^2 + z_diff^2) ** (1./3.), x_diff + y_diff + z_diff)
    # input("wait ...")

    return x_diff + y_diff + z_diff

def str_path(path):
    return str(len(path)) + " " + "".join([n.label for n in path])

def str_paths(paths):
    return "\n".join(str_path(p) for p in paths)

@dataclass
class Node:
    label: str
    x: int
    y: int

    cost = MAX_COST
    est_cost = None
    neighbours = None
    elevation = None
    failed = False
    path = None
    visited = False
    parent = None

    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

        if self.label == "S":
            self.elevation = "a"
        elif self.label == "E":
            self.elevation = "z"
        else:
            self.elevation = self.label
        self.elevation = ord(self.elevation)

    def eligible_neighbours(self, nodes, depth):
        if self.neighbours != None:
            return self.neighbours

        neighbours = []

        # -1, 0
        if self.x > 0:
            neighbour = nodes[self.x-1][self.y]
            if self.update_neighbour_cost(neighbour, depth):
                neighbours.append(neighbour)
        
        # 1, 0
        if self.x < len(nodes) - 1:
            neighbour = nodes[self.x+1][self.y]
            if self.update_neighbour_cost(neighbour, depth):
                neighbours.append(neighbour)

        # 0, -1
        if self.y > 0:
            neighbour = nodes[self.x][self.y-1]
            if self.update_neighbour_cost(neighbour, depth):
                neighbours.append(neighbour)

        # 0, 1
        if self.y < len(nodes[0]) - 1:
            neighbour = nodes[self.x][self.y+1]
            if self.update_neighbour_cost(neighbour, depth):
                neighbours.append(neighbour)

        self.neighbours = neighbours
        return neighbours

    def update_neighbour_cost(self, neighbour, depth):
        z_diff = neighbour.elevation - self.elevation

        if z_diff > 1:
            print(" " * depth, "too big climb!", self.label, neighbour.label, z_diff)
            return False

        h = neighbour.est_cost
        g = self.cost
        cur_cost = h+g

        prev_n_cost = neighbour.cost
        if prev_n_cost < cur_cost:
            print(" " * depth, 'but we already had a better path!', neighbour, prev_n_cost)
            return False

        neighbour.cost = cur_cost
        print(" " * depth, '** we got this', neighbour, cur_cost)
        return True

    def visit(self, nodes, goal_node, fringe=None):
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

        if self == goal_node:
            print(" " * self.depth, self, "victory!!")
            return True, self.parent.path + [self]

        if self.visited:
            print(" " * self.depth, self, 'we already done did this one')
            return False, self.path

        self.visited = True

        neighbours = self.eligible_neighbours(nodes, self.depth)
        if not neighbours:
            print(" " * self.depth, self, "failure.")
            return False, fringe

        for n in neighbours:
            n.parent = self

        if not fringe:
            fringe = neighbours
        else:
            fringe.extend(filter(lambda n: n not in fringe, neighbours))

        sfringe = sorted(fringe, key=lambda n: n.cost)
        print(" " * self.depth, "checking", sfringe)

        if self.parent:
            self.path = self.parent.path + [self]
        else:
            self.path = [self]

        return False, sfringe

def find_char(x, map):
    for i, m in enumerate(map):
        for j, c in enumerate(map[i]):
            if map[i][j] == x:
                return (i, j)

    return None

def find_path(map):
    start = find_char("S", map)
    end = find_char("E", map)

    nodes = []
    for x, line in enumerate(map):
        node_line = []
        for y, c in enumerate(line):
            node_line.append(Node(c, x, y))
        nodes.append(node_line)

    start_node = nodes[start[0]][start[1]]
    start_node.cost = 0

    end_node = nodes[end[0]][end[1]]
    for line in nodes:
        for node in line:
            node.est_cost = estimate_cost(node, end_node)

    fringe = [start_node]
    while fringe:
        node = fringe.pop()

        print(node, fringe)
        input('wait...')
        
        path_found, fringe = node.visit(nodes, end_node, fringe)

        if path_found:
            print_map(nodes, fringe)
            print(len(fringe))

            return len(fringe)

run_test(small_map, 31, find_path)

print(find_path(big_map))




"""
Explanation
A* algorithm has 3 parameters:

g : the cost of moving from the initial cell to the current cell. 
Basically, it is the sum of all the cells that have been visited since leaving the first cell.

h : also known as the heuristic value, it is the estimated cost of 
moving from the current cell to the final cell. The actual cost cannot be 
calculated until the final cell is reached. Hence, h is the estimated cost. 
We must make sure that there is never an over estimation of the cost.

f : it is the sum of g and h. So, f = g + h

The way that the algorithm makes its decisions is by taking the f-value into account. 
The algorithm selects the smallest f-valued cell and moves to that cell. This process 
continues until the algorithm reaches its goal cell."""

