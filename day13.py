from math import floor

# departure = 939
# buses = [7,13,None,None,59,None,31,19]

departure = 1007125
buses = [13,None,None,41,None,None,None,None,None,None,None,None,None,569,None,29,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,19,None,None,None,23,None,None,None,None,None,None,None,937,None,None,None,None,None,37,None,None,None,None,None,None,None,None,None,None,17]

diffs = {}
for bus in buses:
    if bus:
        min = floor(departure / bus)

        print(bus, departure, departure / bus, min, bus * min, departure - bus * min)
        diffs[bus] = bus - (departure - bus * min)

print(diffs)
