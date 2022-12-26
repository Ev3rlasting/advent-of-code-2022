from collections import defaultdict
from copy import deepcopy

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]
YELL = dict()
YELL_TO = defaultdict(list)
G = defaultdict(list)
OPS = dict()
EVAL = []
for line in lines:
    monkey = line[:4]
    ops = line[6:].strip()

    if ops.isnumeric():
        YELL[monkey] = int(ops)
    else:
        G[monkey].extend([ops[:4], ops[-4:]])
        YELL_TO[ops[:4]].append(monkey)
        YELL_TO[ops[-4:]].append(monkey)
        OPS[monkey] = ops[5]
        if monkey == 'root':
            TWO = G[monkey].copy()

one, two = TWO


def topo(g, yells, yell_to, part):
    while 'root' in g:
        for yell in yells.copy():
            shout = yells[yell]
            depend = yell_to[yell][0]
            if yell not in g[depend]: continue
            idx = g[depend].index(yell)
            g[depend][idx] = shout
            if all(isinstance(a, int) or isinstance(a, float) for a in g[depend]):
                yells[depend] = eval(str(g[depend][0]) + OPS[depend] + str(g[depend][1]))
                del g[depend]
    return int(yells['root']) if part == 1 else (yells[one], yells[two])


print('part1', topo(deepcopy(G), deepcopy(YELL), deepcopy(YELL_TO), 1))
N = 3699945358541  # just some run topo calls you will know the range
for i in range(N, N * 2):
    YELL['humn'] = i
    a, b = topo(deepcopy(G), deepcopy(YELL), deepcopy(YELL_TO), 2)
    print(a - b, i)
    if a == b:
        print('part2', a, b, i)
        break
