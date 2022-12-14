import functools
import itertools
import math
from collections import defaultdict, Counter
from functools import cmp_to_key
from pprint import pprint

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]
minY = 500
maxY = 0
maxX = 0

for line in lines:
    points = line.split(' -> ')
    temp = []
    for point in points:
        y, x = list(map(int, point.split(',')))
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        minY = min(minY, y)
print(minY, maxY, maxX)

mat = [["." for _ in range(maxY - minY + 1)] for _ in range(maxX + 1)]

for line in lines:
    points = line.split(' -> ')
    temp = []
    for point in points:
        y, x = list(map(int, point.split(',')))
        y = y - minY
        temp.append((x, y))
    for i in range(len(temp) - 1):
        start, end = sorted([temp[i], temp[i + 1]])
        for i, j in itertools.product(range(start[0], end[0] + 1),
                                      range(start[1], end[1] + 1)):
            mat[i][j] = '#'
# pprint(mat)
START = (0, 500 - minY)

O = set()


def decide(i, j):
    if i < 0 or i == maxX or j < 0 or j == maxY - minY:
        return False
    if mat[i + 1][j] == '.':
        return decide(i + 1, j)  # move down
    if mat[i + 1][j - 1] == '.':
        return decide(i + 1, j - 1)
    if mat[i + 1][j + 1] == '.':
        return decide(i + 1, j + 1)
    else:  # all three slots in the bottom line is filled, fill current slot
        mat[i][j] = 'o'
        O.add((i, j))
        return True


ret = 0
for i in range(1000):
    x, y = START
    rrr = decide(x, y)
    if not rrr:
        print(len(O))
        break
    ret += 1
# pprint(mat)
# print(ret)
