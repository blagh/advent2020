contained_count = 0
overlap_sum = 0

with open("day04input.txt") as file:
    for assignment in file.readlines():
        assignment = assignment[:-1]

        first, secnd = assignment.split(",")
        first = [int(f) for f in first.split("-")]
        secnd = [int(s) for s in secnd.split("-")]

        if first[0] <= secnd[0] and first[1] >= secnd[1] or \
           first[0] >= secnd[0] and first[1] <= secnd[1]:
            contained_count += 1

        first_set = set(range(first[0], first[1] + 1))
        secnd_set = set(range(secnd[0], secnd[1] + 1))

        overlap = len(first_set.intersection(secnd_set))
        if overlap:
            overlap_sum += 1

        print(assignment, overlap)
    
print(contained_count)
print(overlap_sum)