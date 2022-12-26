import heapq
from collections import defaultdict

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]

ret = 0
G = defaultdict(list)
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
    for lead in leads:
        G[v].append(lead)

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


def dfs(curr, minutes, total, remained):
    global ret
    ret = max(ret, total)
    for nxt in remained:
        m = minutes + DIST[(curr, nxt)] + 1
        if m >= 30: continue
        dfs(nxt, m, total + RATES[nxt] * (30 - m + 1), remained - {nxt})

dfs('AA', 1, 0, NONZEROS)
print('part1', ret)
ret = 0

def dfs2(curr1, curr2, min1, min2, total, remained):
    global ret
    ret = max(ret, total)
    for nxt1 in remained:
        for nxt2 in remained:
            if nxt1 == nxt2: continue
            m1 = min1 + DIST[(curr1, nxt1)] + 1
            m2 = min2 + DIST[(curr2, nxt2)] + 1
            if m1 >= 26 or m2 >= 26: continue
            t = total + RATES[nxt1] * (26 - m1 + 1)
            t += RATES[nxt2] * (26 - m2 + 1)
            dfs2(nxt1, nxt2, m1, m2, t, remained - {nxt1, nxt2})

dfs2('AA', 'AA', 1, 1, 0, NONZEROS)
print('part2', ret)