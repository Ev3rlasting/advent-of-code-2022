import collections
import functools
import heapq
import itertools
import json
import math
import sys
from collections import defaultdict, Counter
import functools
from pprint import pprint
from copy import deepcopy
import sys

import yaml

# print(sys.getrecursionlimit())
sys.setrecursionlimit(100000)
f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]
WALL = set()
SNOW = defaultdict(list)
ROAD = {}
for j, line in enumerate(lines):
    for i, ch in enumerate(line):
        if ch == '#':
            WALL.add((i, j))
        elif ch in '><^v':
            SNOW[(i, j)].append(ch)
        else:
            ROAD[(i, j)] = ch
N = len(lines[0])
M = len(lines)
start = (1, 0)
END = (N - 2, M - 1)

def adj(i, j):
    for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if N > a >= 0 and M > b >= 0:
            yield a, b


ret = float('inf')

PROCESSED = dict()


def snowMove(prevSnow):
    snow = prevSnow
    newSnow = defaultdict(list)
    for i, j in snow:
        for ch in snow[(i, j)]:
            ii, jj = i, j
            if ch == '>':
                ii += 1
                if (ii, jj) in WALL:
                    ii = 1
            elif ch == '<':
                ii -= 1
                if (ii, jj) in WALL:
                    ii = N - 2
            elif ch == '^':
                jj -= 1
                if (ii, jj) in WALL:
                    jj = M - 1
                    if (ii, jj) in WALL:
                        jj -= 1
            elif ch == 'v':
                jj += 1
                if (ii, jj) in WALL:
                    jj = 0
                    if (ii, jj) in WALL:
                        jj += 1
            newSnow[(ii, jj)].append(ch)
    # PROCESSED[h] = newSnow
    return newSnow

ret = float('inf')
visited = set()
LIMIT = 300
STATE = None

def dfs(i, j, minute, end, prevSnow):
    global ret, STATE
    if minute > ret or minute > LIMIT: return
    if (i, j) == end:
        if minute < ret:
            ret = minute
            STATE = deepcopy(prevSnow)
        return minute
    minute += 1
    snow = snowMove(prevSnow)

    for a, b in adj(i, j):
        if (a, b, minute) not in visited and (a, b) not in snow and (a, b) not in WALL:
            dfs(a, b, minute, end, snow)
            visited.add((a, b, minute))
    if (i, j) not in snow and (i, j, minute) not in visited:
        dfs(i, j, minute, end, snow)
        visited.add((i, j, minute))


dfs(*start, 0, END, SNOW)
part1 = ret
print('part1', part1)
LIMIT *= 2
ret = float('inf')
visited.clear()
dfs(*END, part1, start, STATE)
part2 = ret
ret = float('inf')
visited.clear()
LIMIT *= 2
dfs(*start, part2, END, STATE)
print('part2', ret)
