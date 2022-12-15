import functools
import itertools
import math
from collections import defaultdict, Counter
from functools import cmp_to_key
from pprint import pprint

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


D = dict()
S = []
B = set()
minX = float('inf')
maxX = -minX
for line in lines:
    line = line.replace('Sensor at x=', '').replace(': closest beacon is at ', ', ').replace('x=', '').replace('y=', '')
    sx, sy, bx, by = list(map(int, line.split(', ')))
    minD = dist(sx, sy, bx, by)
    minX = min(minX, sx, bx)
    maxX = max(maxX, sx, bx)
    D[(sx, sy)] = minD
    S.append((sx, sy))
    B.add((bx, by))

YY = 2000000
ret = set()
for x in range(minX, maxX):
    for sx, sy in S:
        if (x, YY) in B: continue
        if dist(sx, sy, x, YY) <= D[(sx, sy)]:
            # print(x, YY)
            ret.add((x, YY))

print(len(ret))
