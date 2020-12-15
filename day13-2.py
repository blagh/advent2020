from math import floor, lcm
# note: lcm requires python 3.9

def bus_lcm(buses):
    multiple = 1
    length = len(buses)
    print(length, buses)

    while True:
        print(f"{buses[0]}: trying multiple: {multiple} {multiple * buses[0]}")

        it_worked = True
        first_bus = buses[0] * multiple
        first_offset = length - 1
        for i in range(1, length):
            offset = length - i - 1
            this_bus = buses[i]

            # no constraints ~~~
            if this_bus == None:
                # print(f"{i}: skipping None")
                continue

            # if this_bus is exactly what we want, let's take it
            if this_bus + offset == first_bus + first_offset:
                # print(f"{i}: no multiplier needed: {this_bus}:{this_bus + offset} {first_bus}:{first_bus + first_offset}")
                continue

            # if this_bus is greater than next bus + 1, then we can't make it smaller
            if this_bus + offset > first_bus + first_offset:
                # print(f"{i}: this_bus is too big: {this_bus + offset} {first_bus + first_offset}")
                it_worked = False
                break

            # check if we can make a multiple + offset work
            multiplier = int((first_bus + first_offset) / this_bus)
            if this_bus * multiplier + offset == first_bus + first_offset:
                # print(f"{i}: this_bus with a mult: {this_bus * multiplier}:{this_bus * multiplier + offset} {first_bus}:{first_bus + first_offset}")
                continue

            # print(f"{i}: didn't work {this_bus * multiplier}:{this_bus * multiplier + offset} {first_bus}:{first_bus + first_offset}")
            it_worked = False
            break

        if it_worked:
            print(f"Success! {first_bus}")
            return first_bus

        multiple += 1

cases = [
    ([17,None,13,19], 3417),
    ([7,13,None,None,59,None,31,19], 1068781),
    ([67,7,59,61], 754018),
    ([67,None,7,59,61], 779210),
    ([67,7,None,59,61], 1261476),
    ([1789,37,47,1889], 1202161486)
]

for (buses, expected) in cases:
    actual = bus_lcm(buses)
    if expected != actual:
        print("not yet")
        print(expected, actual)
        break
    else:
        print("success!!!")


## FINAL BUSS
final_buss = [13,None,None,41,None,None,None,None,None,None,None,None,None,569,None,29,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,19,None,None,None,23,None,None,None,None,None,None,None,937,None,None,None,None,None,37,None,None,None,None,None,None,None,None,None,None,17]
bus_lcm(final_buss)
