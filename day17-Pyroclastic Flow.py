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

MOVES = lines[0]
ORDER = ['-', '+', '⅃', '|', '#']
# x,y offset to left-bottom point of the rectangle box where the shape is in
SHAPE = {
    '-': ((0 + 0j), (1 + 0j), (2 + 0j), (3 + 0j)),
    '+': ((0 + 1j), (1 + 2j), (1 + 1j), (2 + 1j), (1 + 0j)),
    '⅃': ((0 + 0j), (1 + 0j), (2 + 0j), (2 + 1j), (2 + 2j)),
    '|': ((0 + 0j), (0 + 1j), (0 + 2j), (0 + 3j)),
    '#': ((0 + 0j), (0 + 1j), (1 + 1j), (1 + 0j)),
}

DIR = {
    '>': (1 + 0j),
    '<': (-1 + 0j),
}


def getDots(coord, shape):
    return [dotOffset + coord for dotOffset in SHAPE[shape]]


# coord of the left-bottom point of shape box
def canMove(coord, shape):
    for dot in getDots(coord, shape):
        if dot not in DROPPED and 7 > int(dot.real) >= 0 and int(dot.imag) >= 0:
            continue
        else:
            return False
    return True


def fill(coord, shape):
    h = 0
    for dot in getDots(coord, shape):
        DROPPED.add(dot)
        h = max(h, int(dot.imag) + 1)
    return h


def draw(highest, point, shape):
    dots = getDots(point, shape)
    mat = [['.' for _ in range(7)] for _ in range(highest + 4)]
    for dot in dots:
        mat[~int(dot.imag)][int(dot.real)] = '@'
    for dot in DROPPED:
        mat[~int(dot.imag)][int(dot.real)] = '#'
    started = False
    for line in mat:
        if '@' in line: started = True
        if started:
            print(''.join(line))


DROPPED = set()

highest = 0
n = 0
block = 0
while block < 2024:
    for shape in ORDER:
        block += 1
        prev = highest
        if block == 2023:
            print('part1', highest)
            sys.exit(0)
        point = complex(2, highest + 3)
        print(f'Shape "{shape}" starting at {point}, current stack height: {highest}')
        # draw(highest + 3, point, shape)
        while True:
            direction = DIR[MOVES[n % len(MOVES)]]
            nextJetLocation = point + direction
            if canMove(nextJetLocation, shape):
                point = nextJetLocation
            if canMove(point - 1j, shape):
                point = point - 1j
            else:
                highest = max(highest, fill(point, shape))
                n += 1
                # print(f'\tcurrent point at {point}')
                # draw(highest + 3, point, shape)
                break
            n += 1
            # print(f'\tcurrent point at {point}')
            # draw(highest + 3, point, shape)
