from math import floor

def lcm(buses):
    pass



diffs = {}
for bus in buses:
    if bus:
        min = floor(departure / bus)

        print(bus, departure, departure / bus, min, bus * min, departure - bus * min)
        diffs[bus] = bus - (departure - bus * min)

cases = [
    ([7,13,None,None,59,None,31,19], 1068781),
    ([17,None,13,19], 3417),
    ([67,7,59,61], 754018),
    ([67,None,7,59,61], 779210),
    ([67,7,None,59,61], 1261476),
    ([1789,37,47,1889], 1202161486)
]

for (list, expected) in cases:


## FINAL BUSS
# buses = [13,None,None,41,None,None,None,None,None,None,None,None,None,569,None,29,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,19,None,None,None,23,None,None,None,None,None,None,None,937,None,None,None,None,None,37,None,None,None,None,None,None,None,None,None,None,17]
