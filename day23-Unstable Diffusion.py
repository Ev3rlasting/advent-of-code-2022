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
POS = set()
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch == '#':
            POS.add((j, i))

def adj(i, j):
    for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
                 (i + 1, j + 1), (i + 1, j - 1), (i - 1, j - 1), (i - 1, j + 1)):
        yield a, b

def checkN(i, j):
    for a, b in ((i, j - 1), (i + 1, j - 1), (i - 1, j - 1)):
        yield a, b

def checkS(i, j):
    for a, b in ((i, j + 1), (i + 1, j + 1), (i - 1, j + 1)):
        yield a, b

def checkW(i, j):
    for a, b in ((i - 1, j), (i - 1, j - 1), (i - 1, j + 1)):
        yield a, b

def checkE(i, j):
    for a, b in ((i + 1, j), (i + 1, j - 1), (i + 1, j + 1)):
        yield a, b

DIRECTIONS = collections.OrderedDict({
    'N': [checkN, (0, -1)],
    'S': [checkS, (0, 1)],
    'W': [checkW, (-1, 0)],
    'E': [checkE, (1, 0)]
})

for round in range(30000):
    moved = False
    moves = []
    moveTo = defaultdict(list)
    for x, y in POS:
        if any((a, b) in POS for a, b in adj(x, y)):
            for d, (fn, move) in DIRECTIONS.items():
                if all((a, b) not in POS for a, b in fn(x, y)):
                    moveTo[(x + move[0], y + move[1])].append((x, y))
                    break
    for mt in moveTo:
        if len(moveTo[mt]) == 1:
            moved = True
            POS.discard(moveTo[mt][0])
            POS.add(mt)
    if not moved:
        print('part2', round + 1)
        break
    if round == 9:
        minx = min(x for x, _ in POS)
        maxx = max(x for x, _ in POS)
        miny = min(y for _, y in POS)
        maxy = max(y for _, y in POS)
        print('part1', (maxx - minx + 1) * (maxy - miny + 1) - len(POS))
    DIRECTIONS.move_to_end(list(DIRECTIONS.keys())[0])
