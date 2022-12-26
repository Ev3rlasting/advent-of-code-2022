import sys

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


D = dict()
S = []
B = set()
for line in lines:
    line = line.replace('Sensor at x=', '').replace(': closest beacon is at ', ', ').replace('x=', '').replace('y=', '')
    sx, sy, bx, by = list(map(int, line.split(', ')))
    d = dist(sx, sy, bx, by)
    D[(sx, sy)] = d
    S.append((sx, sy))
    B.add((bx, by))

YY = 4000000

directions = ((-1, -1), (-1, 1), (1, 1), (1, -1))
for sx, sy in S:
    d = D[(sx, sy)] + 1
    start = [sx + d, sy]
    for aa, bb in directions:
        for _ in range(d):
            start[0] += aa
            start[1] += bb
            if (start[0], start[1]) in B or start[0] < 0 or start[0] > YY or start[1] < 0 or start[1] > YY:
                continue
            # check if the point on edge is in no-zone of other beacons
            if all([dist(start[0], start[1], xx, yy) > D[(xx, yy)] for xx, yy in S]):
                print(start[0] * YY + start[1])
                sys.exit(0)
