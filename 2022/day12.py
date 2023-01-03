from collections import defaultdict

MAX_COST = 1_000_000_000

def run_test(input, expected, test_method):
    actual = test_method(input)

    print(input, "\nactual:", actual, "\nexpect:", expected)
    assert(expected == actual)

def print_2d_array(d, path):
    input_string = ""

    min_x = min_y = 0
    max_x = len(d)
    max_y = len(d[0])

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if ([x,y] in path):
                input_string += "*"
            else:
                input_string += str(d[x][y])
        input_string += "\n"

    print(input_string + "-" * max_x + "\n")

def print_2d_defaultdict(d):
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
            if d[x][y] == MAX_COST:
                input_string += "MAX".ljust(15, " ")
            elif d[x][y] != None:
                input_string += ('%.2f' %d[x][y]).ljust(15, " ")
            else:
                input_string += "---".ljust(15, " ")
        input_string += "\n"

    print(input_string + "\n\n")

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

def find_char(x, map):
    for i, m in enumerate(map):
        for j, c in enumerate(map[i]):
            if map[i][j] == x:
                return (i, j)

    return None

def estimate_cost(a_pos, b_pos, map):
    """h : also known as the heuristic value, it is the estimated cost of 
moving from the current cell to the final cell. The actual cost cannot be 
calculated until the final cell is reached. Hence, h is the estimated cost. 
We must make sure that there is never an over estimation of the cost."""

    # let's get euclidean
    x_diff = abs(a_pos[0] - b_pos[0])
    y_diff = abs(a_pos[1] - b_pos[1])

    prev_e = get_from(map, a_pos)
    cur_e = get_from(map, b_pos)
    z_diff = abs(ord(prev_e) - ord(cur_e))

    return (x_diff^2 + y_diff^2 + z_diff^2) ** (1./3.)

def get_from(map, pos):
    e = map[pos[0]][pos[1]]
    if e == "S":
        return "a"
    
    if e == "E":
        return "z"

    return e

def update_cost(prev_pos, cur_pos, goal_pos, costs, map):
    prev_e = get_from(map, prev_pos)
    cur_e = get_from(map, cur_pos)

    z_diff = ord(cur_e) - ord(prev_e)

    if z_diff > 1 or z_diff < -1:
        cur_cost = MAX_COST
        print("too big diff!", prev_e, cur_e, z_diff)
    elif z_diff < 0:
        cur_cost = MAX_COST
        print("let's not go downhill :(", prev_e, cur_e, z_diff)
    else:
        h = estimate_cost(cur_pos, goal_pos, map)
        g = costs[prev_pos[0]][prev_pos[1]]
        cur_cost = h+g
        print("hggg", h, g, cur_cost)

    prev_cur_cost = get_from(costs, cur_pos)

    if prev_cur_cost != None and prev_cur_cost < cur_cost:
        print('but we already had a better path!', prev_cur_cost)
        cur_cost = MAX_COST
    else:
        costs[cur_pos[0]][cur_pos[1]] = cur_cost

    return cur_cost, costs

def update_costs(pos, end, costs, map): 

    print(pos, end, costs, map)

    min_cost = MAX_COST
    min_dir = None

    # -1, 0
    if pos[0] > 0:
        north = [pos[0] - 1, pos[1]]
        print("north", north)
        
        (cost, costs) = update_cost(pos, north, end, costs, map)
        if min_cost > cost:
            min_cost = cost
            min_dir = north

    # 0, 1
    if pos[1] < len(map) - 1:
        west = [pos[0], pos[1] + 1]
        print("west", west)

        (cost, costs) = update_cost(pos, west, end, costs, map)
        if min_cost > cost:
            min_cost = cost
            min_dir = west

    # 1, 0
    if pos[0] < len(map) - 1:
        south = [pos[0] + 1, pos[1]]
        print("south", south)

        (cost, costs) = update_cost(pos, south, end, costs, map)
        if min_cost > cost:
            min_cost = cost
            min_dir = south

    # 0, -1
    if pos[1] > 0:
        east = [pos[0], pos[1] - 1]
        print("east", east)

        (cost, costs) = update_cost(pos, east, end, costs, map)
        if min_cost > cost:
            min_cost = cost
            min_dir = east

    print("the new minimum ~~~", min_cost, min_dir, costs)
    
    return (min_dir, costs)

def find_path(map):
    start = find_char("S", map)
    end = find_char("E", map)

    costs = defaultdict(lambda: defaultdict(lambda: None))
    costs[start[0]][start[1]] = 0

    current = start
    path = [start, get_from(map, start)]
    while current != end:
        (current, costs) = update_costs(current, end, costs, map)

        path.append(current)
        if current:
            path.append(get_from(map, current))

        print("we go:", path)
        print_2d_defaultdict(costs)
        print_2d_array(map, path)
        input("wait ...")

    return costs[end[0]][end[1]]


run_test(small_map, 31, find_path)

find_path(big_map)




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

