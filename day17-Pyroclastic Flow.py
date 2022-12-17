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
# x,y offset to left-bottom point of the rectangle box where the shape is in
SHAPE = {
    '-': ((0, 0), (1, 0), (2, 0), (3, 0)),
    '+': ((0, -1), (1, -2), (1, -1), (2, -1), (1, 0)),
    '⅃': ((0, 0), (1, 0), (2, 0), (2, -1), (2, -2)),
    '|': ((0, 0), (0, -1), (0, -2), (0, -3)),
    '#': ((0, 0), (0, -1), (1, -1), (1, 0)),
}

# x offset of the starting point of the left-bottom rectangle box
START = {
    '-': (2, 0),
    '+': (2, 2),
    '⅃': (2, 2),
    '|': (2, 3),
    '#': (2, 1),
}

DROPPED = {}

highest = 0
n = 0
move = 0
while True:
    for s in ORDER:
        if n == 2023:
            print(highest)
            break
        start_x = START[s]
        start_y = highest + 3

        print(f'Shape {s} starting at {(start_x, start_y)}')
        # shape = SHAPE[s]
        # direction = OPS[move % len(OPS)]
        n += 1

# print(ret)
