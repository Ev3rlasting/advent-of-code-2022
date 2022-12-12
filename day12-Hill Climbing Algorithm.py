import math
from collections import defaultdict, deque
from pprint import pprint
import heapq

f = open('input')
lines = f.readlines()
lines = [list(_.strip()) for _ in lines]

N = len(lines)
M = len(lines[0])
mat = lines


def adj(i, j):
    for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if N > a >= 0 and M > b >= 0:
            yield (a, b)


A = []
for i in range(N):
    for j in range(M):
        if mat[i][j] == 'a':
            A.append((i, j))
        elif mat[i][j] == 'E':
            end = (i, j)
            mat[i][j] = 'z'

ret = float('inf')


def findS(i, j):
    global ret
    q = [(0, (i, j))]
    S = dict()
    while q:
        step, (i, j) = heapq.heappop(q)
        if (i, j) == end:
            ret = min(ret, step)
            break
        for (a, b) in adj(i, j):
            if ord(mat[a][b]) - ord(mat[i][j]) <= 1:
                if S.get((a, b), float('inf')) > step:
                    S[(a, b)] = step
                    heapq.heappush(q, (step + 1, (a, b)))


for (i, j) in A:
    findS(i, j)
print(ret)
