import functools
import itertools
import math
from collections import defaultdict, Counter
from functools import cmp_to_key
from pprint import pprint

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]
maxX = 0

ROCK = set()
for line in lines:
    points = line.split(' -> ')
    temp = []
    for point in points:
        y, x = list(map(int, point.split(',')))
        y = y
        maxX = max(maxX, x)
        temp.append((x, y))
    for i in range(len(temp) - 1):
        start, end = sorted([temp[i], temp[i + 1]])
        for i, j in itertools.product(range(start[0], end[0] + 1),
                                      range(start[1], end[1] + 1)):
            ROCK.add((i, j))

START = (0, 500)
ret = 0
INF = maxX + 1
def decide(i, j):
    global ret
    if (i + 1, j) not in ROCK and i < INF:
        return decide(i + 1, j)  # move down
    if (i + 1, j - 1) not in ROCK and i < INF:  # move left
        return decide(i + 1, j - 1)
    if (i + 1, j + 1) not in ROCK and i < INF:  # move right
        return decide(i + 1, j + 1)
    if i + 1 == INF:  # reach the inf wall
        ROCK.add((i, j))
        ret += 1
        return True
    else:  # all three slots in the bottom line is filled, fill current slot
        ROCK.add((i, j))
        ret += 1
        return True

for i in range(10000000):
    x, y = START
    rrr = decide(x, y)
    if START in ROCK:
        print(ret)
        break
