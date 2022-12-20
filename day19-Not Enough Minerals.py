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

ret = 0
BLUEPRINTS = []
for line in lines:
    line = line.replace('Blueprint ', '').replace('Each ore robot costs ', '') \
        .replace('Each clay robot costs ', '') \
        .replace('Each obsidian robot costs ', '') \
        .replace('Each geode robot costs ', '') \
        .replace('.', ',').replace('obsidian,', 'obsidian')
    config = line.split(', ')
    c1 = int(config[0][:5].split(': ')[1].strip())
    c2 = int(config[1][:5].replace(' ore', '').strip())
    c3 = list(map(int, (config[2].replace('ore and', ',').replace(' clay', '').split(','))))
    c4 = list(map(int, (config[3].replace('ore and', ',').replace(' obsidian', '').split(','))))
    # print(c1, c2, c3, c4)
    BLUEPRINTS.append(((c1, 0, 0), (c2, 0, 0), (c3[0], c3[1], 0), (c4[0], 0, c4[1])))
pprint(BLUEPRINTS)


# @functools.lru_cache(maxsize=None)
def dfs(r0, r1, r2, r3, b0, b1, b2, b3, blueprint, minute):
    global ret
    if minute == 24 and b3 == 0: return 0
    if minute == 22 - blueprint[3][2] and b2 == 0:
        return 0
    if minute == 21 - blueprint[2][1] - blueprint[3][2] and b1 == 0:
        return 0
    if minute == 25:
        print(f'min {minute}\t r0 {r0}\t r1 {r1}\t r2 {r2}\t r3 {r3}\t b0 {b0}\t b1 {b1}\t b2 {b2}\t b3 {b3}')
        return r3
    if minute > 23 and b3 == 0: return 0

    p0 = p1 = p2 = p3 = p4 = 0
    if r2 >= blueprint[3][2] and r0 >= blueprint[3][0]:
        p0 = dfs(r0 - blueprint[3][0] + b0, r1 + b1, r2 - blueprint[3][2] + b2, r3 + b3, b0, b1, b2, b3 + 1, blueprint,
                 minute + 1)
    if r1 >= blueprint[2][1] and r0 >= blueprint[2][0]:
        p1 = dfs(r0 - blueprint[2][0] + b0, r1 - blueprint[2][1] + b1, r2 + b2, r3 + b3, b0, b1, b2 + 1, b3, blueprint,
                 minute + 1)
    if r0 >= blueprint[1][0]:
        p2 = dfs(r0 - blueprint[1][0] + b0, r1 + b1, r2 + b2, r3 + b3, b0, b1 + 1, b2, b3, blueprint, minute + 1)
    if r0 >= blueprint[0][0]:
        p3 = dfs(r0 - blueprint[0][0] + b0, r1 + b1, r2 + b2, r3 + b3, b0 + 1, b1, b2, b3, blueprint, minute + 1)
    p4 = dfs(r0 + b0, r1 + b1, r2 + b2, r3 + b3, b0, b1, b2, b3, blueprint, minute + 1)
    return max(p0, p1, p2, p3, p4)


for idx, blueprint in enumerate(BLUEPRINTS[:-1]):
    idx += 1
    ret = dfs(0, 0, 0, 0, 2, 0, 0, 0, blueprint, 2)
    print(ret)
# for idx, blueprint in enumerate(BLUEPRINTS[:-1]):
#     idx += 1
#     # ore = clay = obs = geo = 0
#     q_resource = [1, 0, 0, 0]
#     q_bots = [1, 0, 0, 0]
#     for min in range(2, 25):
#         r0, r1, r2, r3 = q_resource
#         b0, b1, b2, b3 = q_bots
#         if r2 >= blueprint[3][2] and r0 >= blueprint[3][0]:
#             r2 -= blueprint[3][2]
#             r0 -= blueprint[3][0]
#             b3 += 1
#         elif r1 >= blueprint[2][1] and r0 >= blueprint[2][0]:
#             r1 -= blueprint[2][1]
#             r0 -= blueprint[2][0]
#             b2 += 1
#         elif r0 >= blueprint[1][0]:
#             r0 -= blueprint[1][0]
#             b1 += 1
#         elif r0 >= blueprint[0][0]:
#             r0 -= blueprint[0][0]
#             b0 += 1
#         q_resource = [r0, r1, r2, r3]
#         q_resource[0] += q_bots[0]
#         q_resource[1] += q_bots[1]
#         q_resource[2] += q_bots[2]
#         q_resource[3] += q_bots[3]
#         q_bots = [b0, b1, b2, b3]
#         print(min)
#         print(q_resource)
#         print(q_bots)
#         print()
