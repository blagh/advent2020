from collections import defaultdict

starting = [None, 8,13,1,0,18,9]
seen = {starting[i]: i for i in range(len(starting))}
print(seen)

max_n = 30_000_000
n = len(starting)
last_number = 0
while n <= max_n:
    print(f"{int(n / max_n * 100)}%: {last_number}")

    if seen.get(last_number) is None:
        # print(f"it's a new number: {last_number}")
        seen[last_number] = n
        last_number = 0
    else:
        # print(f"got last numbers: {last_number} {seen[last_number]}")

        next_number = n - seen[last_number]
        seen[last_number] = n

        last_number = next_number

    n += 1

# print(last_number)
