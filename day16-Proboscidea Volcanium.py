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

ret = 0
G = defaultdict(list)
OPEN = set()
CLOSE = set()
RATES = dict()
for line in lines:
    line = line.replace('Valve ', '').replace(' has flow rate=', ' ') \
        .replace('tunnel leads to valve ', 'tunnels lead to valves ') \
        .replace('tunnels lead to valve ', 'tunnels lead to valves ') \
        .replace('; tunnels lead to valves ', ' ') \
        .replace(', ', ',')
    v, rate, leads = line.split(' ')
    rate = int(rate)
    RATES[v] = rate
    leads = leads.split(',')
    CLOSE.add(v)
    for lead in leads:
        G[v].append(lead)

# pprint(G)
DIST = dict()
ALL_NODES = G.keys()


def get_dist(start, end):
    if start == end: return 0
    q = [(0, start)]
    visited = set()
    while q:
        dist, node = heapq.heappop(q)
        if node == end:
            return dist
        visited.add(node)
        for nxt in G[node]:
            if nxt not in visited:
                heapq.heappush(q, (dist + 1, nxt))
    return float('inf')


for i in ALL_NODES:
    for j in ALL_NODES:
        DIST[(i, j)] = get_dist(i, j)

NONZEROS = {node for node in ALL_NODES if RATES[node] > 0}

remained = NONZEROS

def dfs(curr, minutes, total, remained, path):
    global ret
    ret = max(ret, total)
    for nxt in remained:
        m = minutes + DIST[(curr, nxt)] + 1
        if m >= 30: continue
        dfs(nxt, m,
            total + RATES[nxt] * (30 - m + 1),
            remained - {nxt},
            path + [(nxt, minutes + DIST[(curr, nxt)] + 1)])


dfs('AA', 1, 0, NONZEROS, [])
pprint(DIST)
print(ret)
