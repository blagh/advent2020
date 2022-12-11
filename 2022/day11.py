from dataclasses import dataclass, field
from functools import reduce

@dataclass
class Monkey:
    items: list
    operation: "typing.Any" = field(repr=False)
    test_divisor: int = field(repr=False) 
    true_monkey: int = field(repr=False)
    false_monkey: int = field(repr=False)

    inspected: int = 0

    def inspect(self, mega_modulo):
        self.inspected += len(self.items)
        self.items = list(
            map(lambda x: x % mega_modulo, 
                map(self.operation, self.items)
            )
        )

    def throw(self, monkeys):
        for i in self.items:
            if i % self.test_divisor == 0:
                monkeys[self.true_monkey].items.append(i)
            else:
                monkeys[self.false_monkey].items.append(i)

        self.items = []

def round(monkeys, mega_modulo):
    for m in monkeys:
        m.inspect(mega_modulo)
        m.throw(monkeys)

    # for m in monkeys:
    #     print(m)

monkeys = [
    Monkey([79, 98], lambda x: x * 19, 23, 2, 3),
    Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0),
    Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3),
    Monkey([74], lambda x: x + 3, 17, 0, 1)
]

MEGA_MODULO = reduce(lambda acc, m: acc * m.test_divisor, monkeys, 1)

for i in range(1, 10001):
    # print("round", i, MEGA_MODULO)
    round(monkeys, MEGA_MODULO)

inspections = sorted(map(lambda m: m.inspected, monkeys))

print(inspections[-1], inspections[-2])
print(inspections[-1] * inspections[-2])

monkeys = [
    Monkey([54, 98, 50, 94, 69, 62, 53, 85], lambda x: x * 13, 3, 2, 1, ),
    Monkey([71, 55, 82], lambda x: x + 2, 13, 7, 2),
    Monkey([77, 73, 86, 72, 87], lambda x: x + 8, 19, 4, 7),
    Monkey([97, 91], lambda x: x + 1, 17, 6, 5),
    Monkey([78, 97, 51, 85, 66, 63, 62], lambda x: x * 17, 5, 6, 3),
    Monkey([88], lambda x: x + 3, 7, 1, 0),
    Monkey([87, 57, 63, 86, 87, 53], lambda x: x * x, 11, 5, 0),
    Monkey([73, 59, 82, 65], lambda x: x + 6, 2, 4, 3)
]

MEGA_MODULO = reduce(lambda acc, m: acc * m.test_divisor, monkeys, 1)

print(monkeys)

for i in range(1, 10):
    print("round", i)
    round(monkeys, MEGA_MODULO)
    print(monkeys)

inspections = sorted(map(lambda m: m.inspected, monkeys))

print(inspections[-1], inspections[-2])
print(inspections[-1] * inspections[-2])