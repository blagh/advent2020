class Node:
    def __init__(self, name):
        self.visited = False
        self.name = name
        self.neighbours = []

    def add_neighbour(self, node):
        self.neighbours.append(node)

    def is_entrance(self):
        return self.name == "start"

    def _is_exit(self):
        return self.name == "end"

    def _is_big_cave(self):
        return self.name.isupper()

    def _can_visit(self):
        return self._is_big_cave() or not self.visited

    def visit(self):
        if not self._can_visit():
            return 0

        if self._is_exit():
            return 1

        self.visited = True
        path_count = 0
        for node in self.neighbours:
            path_count += node.visit()

        self.visited = False
        return path_count

    def __repr__(self):
        return self.name + ": " + " ".join([n.name for n in self.neighbours])

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
