lines = open('input').readlines()
lines = [_.strip() for _ in lines]
N = len(lines)
M = len(lines[0])
mat = [[] for _ in range(N)]
for idx, line in enumerate(lines):
    mat[idx].extend(list(map(int, line)))
ret = 0
seen = set()


def check_top(i, j):
    r = 0
    ii = i - 1
    while ii >= 0 and mat[ii][j] < mat[i][j]:
        r += 1
        ii -= 1
    if ii >= 0: r += 1
    return r


def check_down(i, j):
    r = 0
    ii = i + 1
    while ii < M and mat[ii][j] < mat[i][j]:
        r += 1
        ii += 1
    if ii < M: r += 1
    return r


def check_left(i, j):
    r = 0
    jj = j - 1
    while jj >= 0 and mat[i][jj] < mat[i][j]:
        r += 1
        jj -= 1
    if jj >= 0: r += 1
    return r


def check_right(i, j):
    r = 0
    jj = j + 1
    while jj < N and mat[i][jj] < mat[i][j]:
        r += 1
        jj += 1
    if jj < N: r += 1
    return r


for i in range(N):
    for j in range(M):
        score = check_top(i, j) * check_down(i, j) * check_left(i, j) * check_right(i, j)
        ret = max(ret, score)

print(ret)
