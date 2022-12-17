import functools
import heapq
import itertools
import math
import sys
from collections import defaultdict, Counter
from functools import cmp_to_key
from pprint import pprint

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]

OPS = lines[0]
ORDER = ['-', '+', '⅃', '|', '#']
SHAPE = {
    '-': ((0, 0), (0, 1), (0, 2), (0, 3)),
    '+': ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
    '⅃': ((0, 2), (1, 2), (2, 0), (2, 1), (2, 2)),
    '|': ((0, 0), (1, 0), (2, 0), (3, 0)),
    '#': ((0, 0), (0, 1), (1, 0), (1, 1)),
}

LEFT_DOWN = {
    '-': (2, 0),
    '+': (3, 2),
    '⅃': (4, 2),
    '|': (2, 3),
    '#': (2, 1)
}

DROPPED = {}

def drop(shape, i, j):




ret = 0
n = 0
move = 0
while True:
    for o in ORDER:
        if n == 2023:
            print(ret)
            break
        start_y, start_x = START[o][0], ret - START[o][0]

        shape = SHAPE[o]
        direction = OPS[move % len(OPS)]
        n += 1

print(ret)
