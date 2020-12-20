lines = []

with open("day10input.txt") as file:
    lines = file.readlines()

lines = [int(l[:-1]) for l in lines]
lines = sorted(lines)
lines = lines + [lines[-1] + 3]

one_diffs = 0
three_diffs = 0
prev_number = 0

for n in lines:
    if n - prev_number == 1:
        one_diffs += 1
    elif n - prev_number == 3:
        three_diffs += 1
    prev_number = n


print(one_diffs, three_diffs)


# loool this complicated shit for a sorted list
# def compatible(n, lines):
#     return list(filter(lambda x: x != n and x >= n-3 and x <= n+3, lines))
# nodes = {l: compatible(l, lines) for l in lines}
#
#
# def find_sequence(n, nodes, visited=None):
#     if visited is None:
#         print("0: ", n, nodes, visited)
#         visited = [n]
#
#     if len(visited) == len(nodes):
#         return visited
#
#     print("1: ", n, nodes, visited)
#
#     sub_seq = []
#     for c in nodes[n]:
#         if c in visited:
#             continue
#
#         sub_seq = find_sequence(c, nodes, visited + [c])
#         if sub_seq == []:
#             print("2: ", sub_seq, visited, nodes, "\n")
#             continue
#
#         # we've found a sub-sequence of an appropriate length
#         print("3: ", sub_seq, visited, nodes)
#         if (len(sub_seq) == len(nodes)):
#             return sub_seq
#
#     # no sub-sequence was found
#     return []
#
#     print(n, nodes, visited)
#
# print(find_sequence(lines[0], nodes))



# def find_sequence(n, lines):
#     print(n, lines)
#     if (lines == []):
#         return [n]
#
#     chargers = []
#     for l in lines:
#         compats = compatible(l, lines)
#         if compats == []:
#             return []
#
#         sub_seq = []
#         for c in compats:
#             line_copy = lines[:]
#             line_copy.remove(c)
#             sub_seq = find_sequence(c, line_copy)
#             if sub_seq == []:
#                 continue
#
#         if sub_seq == []:
#             return []
#         else:
#             return sub_seq + [l]
