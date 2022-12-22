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
# lines = [_.strip() for _ in lines]
TILES = set()
WALLS = set()
first = None
for i, line in enumerate(lines):
    if line == '\n':
        MOVES = lines[i + 1]
        break
    for j, ch in enumerate(line):
        if ch == '#':
            WALLS.add((i, j))
        elif ch == '.':
            if not first:
                first = (i, j)
            TILES.add((i, j))

print(TILES)
print(WALLS)

