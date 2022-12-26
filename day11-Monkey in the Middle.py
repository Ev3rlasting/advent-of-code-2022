from collections import defaultdict

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

# pls adjust below dict to your test case
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

FN = OPS_2

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

MOD = 1
for prime, _, _ in DIV.values():
    MOD *= prime

print(MOD)

inspect = [0 for _ in range(len(MONKEYS))]
for i in range(10000):
    for monkey in MONKEYS:
        inspect[monkey] += len(MONKEYS[monkey])
        for item in MONKEYS[monkey]:
            worry = FN[monkey](item) % MOD
            if worry % DIV[monkey][0] == 0:
                nextMonkey = DIV[monkey][1]
            else:
                nextMonkey = DIV[monkey][2]
            MONKEYS[nextMonkey].append(worry)
        MONKEYS[monkey].clear()


print(inspect)
inspect.sort()
print(inspect[-1] * inspect[-2])
