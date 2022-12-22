f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]
def adj(i, j, k):
    for a, b, c in ((i + 1, j, k), (i - 1, j, k), (i, j + 1, k), (i, j - 1, k), (i, j, k + 1), (i, j, k - 1)):
        if all(22 >= i >= -2 for i in (a, b, c)):
            yield a, b, c

OCCUPIED = set()
for line in lines:
    x, y, z = list(map(int, line.split(',')))
    OCCUPIED.add((x, y, z))
ret = 0
for x, y, z in OCCUPIED:
    k = 6
    for a, b, c in adj(x, y, z):
        if (a, b, c) in OCCUPIED:
            k -= 1
    ret += k
print('part1', ret)

q = [(-1, -1, -1)]
visited = set()
touched = set()
while q:
    x, y, z = q.pop()
    visited.add((x, y, z))
    for a, b, c in adj(x, y, z):
        if (a, b, c) not in visited:
            if (a, b, c) in OCCUPIED:
                touched.add(tuple(sorted([(a, b, c), (x, y, z)])))
            else:
                q.append((a, b, c))
print('part2', len(touched))
