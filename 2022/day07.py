from dataclasses import dataclass

@dataclass
class Directory:
    label: str
    parent = None
    children = None
    files = None
    _size = None

    def __init__(self, label):
        self.label = label
        self.parent = None
        self.children = {}
        self.files = []

    def add_child(self, child_label):
        child = Directory(child_label)
        child.parent = self

        self.children[child_label] = child

    def add_file(self, file_name, file_size):
        self.files.append(File(file_name, file_size))

    def size(self):
        if self._size != None:
            return self._size

        file_size = sum([f.size for f in self.files])
        chld_size = sum([c.size() for c in self.children.values()])

        self._size = file_size + chld_size
        return self._size

    def to_string(self, depth=0):
        if depth > 5:
            return "~ oh no ~"

        self_str = "  " * depth + "- " + self.label + " (dir, size=" + str(self.size()) + ")\n"
        #print(depth, self_str)

        for c in self.children.values():
            #print(c, self.children)
            self_str += c.to_string(depth+1)

        for f in self.files:
            self_str += f.to_string(depth+1)

        return self_str

@dataclass
class File:
    name: str
    size: int

    def to_string(self, depth):
        return "  " * depth + "- " + self.name + " (file, size=" + str(self.size) + ")" + "\n"

root_dir = Directory("/")

with open("day07input.txt") as file:
    working = root_dir
    listing = False

    for line in file.readlines():
        tokens = line[:-1].split(" ")
        print(tokens)

        if tokens[0] == "$":
            listing = False
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    working = working.parent
                elif tokens[2] == "/":
                    pass
                else:
                    working = working.children[tokens[2]]
            if tokens[1] == "ls":
                listing = True
            
        elif listing: 
            if tokens[0] == "dir":
                working.add_child(tokens[1])
            else:
                working.add_file(tokens[1], int(tokens[0]))

        print(working, working.children)

print("-----")
print(root_dir.to_string())
print(root_dir.size())

less_than_100000_sum = 0

def sum_less_than_100000(directory):
    summ = 0

    if directory.size() < 100_000:
        summ += directory.size()

    for c in directory.children.values():
        summ += sum_less_than_100000(c)

    return summ

print(sum_less_than_100000(root_dir))

total_disk_space = 70000000
space_free = total_disk_space - root_dir.size()
required_space = 30000000
space_to_free = required_space - space_free

print(total_disk_space, "must free", space_to_free)

def find_next_largest_dir(directory, target_size, depth=0):
    next_largest = directory.size()
    if next_largest < target_size:
        return 0

    print(" " * depth + "parent:", directory.label, next_largest)
    for c in directory.children.values():

        child_size = find_next_largest_dir(c, space_to_free, depth+1)
        print("   " * depth + "  child:", c.label, child_size)

        if child_size > target_size and child_size < next_largest:
            next_largest = child_size
            

    print(" " * depth + "parent:", directory.label, next_largest)
    return next_largest

print(space_to_free, find_next_largest_dir(root_dir, space_to_free))