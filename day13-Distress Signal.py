import functools
import math
from collections import defaultdict, Counter
from functools import cmp_to_key
from pprint import pprint

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]
lines.append("")
A = []

ret = 0


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a > b:
            return 1
        return 0

    if not isinstance(a, list):
        return compare([a], b)
    if not isinstance(b, list):
        return compare(a, [b])

    i = 0
    while i < len(a) and i < len(b):
        ret = compare(a[i], b[i])
        if ret != 0:
            return ret
        i += 1
    if len(a) > len(b):
        return 1
    if len(a) == len(b):
        return 0
    if len(a) < len(b):
        return -1


i = 0
for line in lines:
    if line:
        i += 1
        A.append(eval(line))

B = [[2], [6]]
A.extend(B)
A.sort(key=cmp_to_key(compare))
ret = 1
for idx, a in enumerate(A):
    if a in B:
        ret *= idx + 1

print(ret)
