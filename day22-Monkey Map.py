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
mat = []
N = len(lines[0].replace('\n', ''))
print(N)
for j, line in enumerate(lines):
    if line == '\n':
        MOVES = lines[j + 1]
        break
    row = []
    line = line.ljust(N+1)
    for i, ch in enumerate(line):
        if ch != '\n':
            if ch == '.' and not first:
                first = (i, j)
            row.append(ch)
    mat.append(''.join(row))

direction = (1, 0)
TURN = {
    (1, 0): {'R': (0, 1),
             'L': (0, -1)
             },
    (0, 1): {'R': (-1, 0),
             'L': (1, 0)
             },
    (-1, 0): {'R': (0, -1),
              'L': (0, 1)
              },
    (0, -1): {'R': (1, 0),
              'L': (-1, 0)
              },
}

# pprint(mat)
print('start at ', first)


def move(point, direction, step):
    x, y = point
    dx, dy = direction
    prevOk = (x, y)
    while step > 0:
        print('\t', x, y)
        x += dx
        y += dy
        if x == len(mat[0]):
            x = 0
        elif x < 0:
            x = len(mat[0]) - 1
        elif y == len(mat):
            y = 0
        elif y < 0:
            y = len(mat) - 1
        print('\t\tchecking #', x, y)
        if mat[y][x] == '#':
            return prevOk
        if mat[y][x] == ' ':
            continue
        step -= 1
        prevOk = (x, y)
    return x, y


s = ''
point = first
for ch in MOVES + 'L':
    if ch in 'RL':
        step = int(s)
        lastDir = direction
        print('move:', direction, step, 'then turn:', TURN[direction][ch])
        point = move(point, direction, step)
        print('point', point)
        s = ''
        direction = TURN[direction][ch]
    else:
        s += ch
print(point, lastDir)
# print(TILES)
# print(WALLS)
print((point[0] + 1) * 4 + (point[1] + 1) * 1000 + list(TURN).index(lastDir))
