from functools import reduce
from math import floor, lcm

# sauce: https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n,a):
        p = prod // n_i # for large p
        sum += a_i * mul_inv(p, n_i) * p

    return sum, prod, sum % prod

def mul_inv(a, b):
    if b == 1: return 1

    b0 = b
    x0, x1 = 0,1
    while a > 1:
        q = a // b
        (a, b) = (b, a % b)
        x0, x1 = x1 - q * x0, x0

    if x1 < 0: x1 += b0
    return x1

def bus_lcm(buses):
    n = []
    a = []
    for i in range(len(buses)):
        if buses[i]:
            n.append(buses[i])
            a.append(i)

    print(n, a)
    (sum, prod, mod_prod) = chinese_remainder(n, a)
    return prod - mod_prod

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
print(bus_lcm(final_buss))
