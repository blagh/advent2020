class Node:
    def __init__(self, name):
        self.visited = 0
        self.name = name
        self.neighbours = []

    def add_neighbour(self, node):
        self.neighbours.append(node)

    def _is_entrance(self):
        return self.name == "start"

    def _is_exit(self):
        return self.name == "end"

    def _is_big_cave(self):
        return self.name.isupper()

    def _can_visit(self, can_double_visit):
        if self._is_big_cave():
            return True

        if self._is_entrance() or not can_double_visit:
            return self.visited < 1

        return self.visited < 2

    def visit(self, can_double_visit=True, depth=0):
        if not self._can_visit(can_double_visit):
            # print(' ' * depth, self.name, 'noope')
            return 0

        if self._is_exit():
            print(' ' * depth, "exit!! +1")
            return 1

        print(' ' * depth, "--", self.name, ":", self.visited, "--")
        pre_visit = self.visited

        self.visited += 1
        if not self._is_big_cave() and self.visited == 2:
            print(' ' * depth, 'dubla!')
            can_double_visit = False

        path_count = 0
        for node in self.neighbours:
            path_count += node.visit(can_double_visit, depth + 1)
        else:
            pass
            # print(' ' * depth, 'all done, counted', path_count)

        self.visited = pre_visit
        return path_count

    def __repr__(self):
        return repr(self.visited) + " " + self.name + ": " + " ".join([n.name for n in self.neighbours])

NODES = {}

def add_node_if_needed(name):
    if name in NODES:
        return NODES[name]

    node = Node(name)
    NODES[name] = node
    return node

with open("day12.txt") as file:
    for line in file.readlines():
        (start, end) = line[:-1].split("-")

        start = add_node_if_needed(start)
        end = add_node_if_needed(end)

        start.add_neighbour(end)
        end.add_neighbour(start)

print("\n".join([str(n) for n in list(NODES.values())]))
path_count = NODES["start"].visit()
print(path_count)
