import math
from collections import defaultdict
from pprint import pprint

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]
lines.append("")
OPS_1 = {
    0: lambda x: x * 19,
    1: lambda x: x + 6,
    2: lambda x: x ** 2,
    3: lambda x: x + 3
}

OPS_2 = {
    0: lambda x: x * 11,
    1: lambda x: x + 8,
    2: lambda x: x * 3,
    3: lambda x: x + 4,
    4: lambda x: x ** 2,
    5: lambda x: x + 2,
    6: lambda x: x + 3,
    7: lambda x: x + 5,

}

OPS = OPS_1

MONKEYS = defaultdict(list)
DIV = dict()

for line in lines:
    if line.startswith('Monkey'):
        monkey = int(line[7])
    elif line.startswith("Starting items:"):
        starting_items = list(map(int, line[16:].split(', ')))
    elif line.startswith("Test: divisible by "):
        divisible = int(line[19:])
    elif line.startswith('If true: throw to monkey '):
        trueTo = int(line[25:])
    elif line.startswith('If false: throw to monkey '):
        falseTo = int(line[26:])
    elif line == "":
        MONKEYS[monkey].extend(starting_items)
        DIV[monkey] = (divisible, trueTo, falseTo)
        print(f' Monkey: {monkey}'
              f' starting items: {starting_items}'
              f' divisible: {divisible}'
              f' True: {trueTo}, False: {falseTo}')
pprint(MONKEYS)
pprint(DIV, width=20)

round = 0
inspect = [0 for _ in range(len(MONKEYS))]

while round < 1000:
    for monkey in sorted(MONKEYS.keys()):
        items = MONKEYS[monkey]
        if len(items) == 1:
            print(monkey)
        # print(items)
        inspect[monkey] += len(items)
        for item in items:
            worry = OPS[monkey](item)
            worry = int(math.floor(worry / 3))
            if worry % DIV[monkey][0] == 0:
                MONKEYS[DIV[monkey][1]].append(worry)
            else:
                MONKEYS[DIV[monkey][2]].append(worry)
        MONKEYS[monkey].clear()
    # pprint(MONKEYS)
    round += 1
# pprint(MONKEYS)
# pprint(inspect)
inspect.sort()
print(inspect[-1] * inspect[-2])
