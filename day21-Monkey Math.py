import collections
import functools
import heapq
import itertools
import math
import sys
from collections import defaultdict, Counter
import functools
from pprint import pprint
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


def topo(g, yells, yell_to):
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
    return yells['root']


one, two = TWO


def topo2(g, yells, yell_to):
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
    return yells[one], yells[two]


N = 3699945358541 # just some run topo2 you will know the pattern
for i in range(N, N * 2):
    YELL['humn'] = i
    a, b = topo2(deepcopy(G), deepcopy(YELL), deepcopy(YELL_TO))
    print(a - b, i)
    if a == b:
        print('part2', a, b, i)
        break
