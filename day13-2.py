from math import floor, lcm
# note: lcm requires python 3.9

def bus_lcm(buses):

    length = len(buses)
    new_buses = []
    for i in range(len(buses)):
        if buses[i]:
            new_buses.append(buses[i] + length - i - 1)

    print(buses, new_buses)
    return lcm(*new_buses) - length

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


## FINAL BUSS
# buses = [13,None,None,41,None,None,None,None,None,None,None,None,None,569,None,29,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,19,None,None,None,23,None,None,None,None,None,None,None,937,None,None,None,None,None,37,None,None,None,None,None,None,None,None,None,None,17]
