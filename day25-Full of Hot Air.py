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
f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]
MAP = {
    '=': -2,
    '-': -1
}

RULE = {
    3: (1, '='),
    4: (1, '-'),
    5: (1, 0),
    -1: (0, '-'),
    -2: (0, '='),
    -3: (-1, 2),
    -4: (-1, 1),
    -5: (-1, 0)
}


def add(a, b):
    short, long = (a, b) if len(a) <= len(b) else (b, a)
    short = short[::-1]
    long = long[::-1]
    i = 0
    s = []
    carry = 0
    while i < len(long):
        if i < len(short):
            summ = int(MAP.get(short[i], short[i])) + int(MAP.get(long[i], long[i])) + carry
        else:
            summ = int(MAP.get(long[i], long[i])) + carry
        if 0 <= summ <= 2:
            carry, digit = 0, summ
        else:
            carry, digit = RULE[summ]
        s.append(digit)
        i += 1
    if carry != 0:
        if carry > 0:
            s.append(carry)
        elif carry == -1:
            s.append('=')
        else:
            s.append('-')
    return ''.join(list(map(str, s))[::-1])
ret = lines[0]
for line in lines[1:]:
    ret = add(ret, line)
print('part1', ret)
