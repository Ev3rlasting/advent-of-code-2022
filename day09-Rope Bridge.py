lines = open('input').readlines()
lines = [_.strip() for _ in lines]
directions = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0),
}

strategy = {
    (2, -2): (1, -1),
    (2, -1): (1, -1),
    (2, 0): (1, 0),
    (2, 1): (1, 1),
    (2, 2): (1, 1),
    (-2, -2): (-1, -1),
    (-2, 0): (-1, 0),
    (-2, -1): (-1, -1),
    (-2, 1): (-1, 1),
    (-2, 2): (-1, 1),
    (0, 2): (0, 1),
    (0, -2): (0, -1),
    (1, 2): (1, 1),
    (-1, 2): (-1, 1),
    (1, -2): (1, -1),
    (-1, -2): (-1, -1),
}

H = (0, 0)
tails = [H for _ in range(10)]
visited = {H}

for line in lines:
    d, steps = line.split(' ')
    for i in range(int(steps)):
        a, b = directions[d]
        H = (H[0] + a, H[1] + b)
        tails[-1] = H
        for j in reversed(range(9)):
            dist = (tails[j + 1][0] - tails[j][0], tails[j + 1][1] - tails[j][1])
            if dist in strategy:
                tails[j] = (tails[j][0] + strategy[dist][0], tails[j][1] + strategy[dist][1])
        visited.add(tails[0])
print(len(visited))
