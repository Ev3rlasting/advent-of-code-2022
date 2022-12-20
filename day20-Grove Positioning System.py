import collections
import functools
import heapq
import itertools
import math
import sys
from collections import defaultdict, Counter
import functools
from pprint import pprint

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]

A = []

for idx, line in enumerate(lines):
    if line == '0':
        ZERO = (0, idx)
    A.append((int(line) * 811589153, idx))

O = A.copy()
for _ in range(10):
    for i, o in enumerate(O):
        if o[0] == 0: continue
        idx = A.index(o)
        A.pop(idx)
        newIdx = (idx + o[0]) % len(A)
        A = A[:newIdx] + [o] + A[newIdx:]
        # print(A)
zero = A.index(ZERO)
r1 = A[(zero + 1000) % len(A)]
r2 = A[(zero + 2000) % len(A)]
r3 = A[(zero + 3000) % len(A)]
print(r1, r2, r3)
print('part2', r1[0] + r2[0] + r3[0])
