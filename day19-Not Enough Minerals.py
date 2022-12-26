import functools
import gc

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]


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
# pprint(BLUEPRINTS)

MIN = 32

@functools.lru_cache(maxsize=None)
def dfs(r0, r1, r2, r3,
        b0, b1, b2,
        m0, m1, m2,
        best_sofar, blueprint, minute):
    # print(f'min {minute}\t r0 {r0}\t r1 {r1}\t r2 {r2}\t r3 {r3}\t b0 {b0}\t b1 {b1}\t b2 {b2}\t b3 {b3}')
    if minute == MIN: return r3
    p0 = p1 = p2 = p3 = p4 = 0
    minute += 1
    t = MIN - minute
    # assume from now on you have *infinite* resource and start to build geodes bot every future minute,
    # can it beat the best_sofar? If not, stop trying
    if t * (t + 1) // 2 + r3 <= best_sofar: return r3
    # build geode robot (b3)
    if r2 >= blueprint[3][2] and r0 >= blueprint[3][0]:
        # always build geode robot, dont try other options (not sure if it works for all inputs but ok for me)
        return dfs(r0 - blueprint[3][0] + b0, r1 + b1, r2 - blueprint[3][2] + b2, r3 + t,
                   b0, b1, b2,
                   m0, m1, m2,
                   max(best_sofar, r3 + t), blueprint, minute)

    # build obsidian robot (b2)
    if r1 >= blueprint[2][1] and r0 >= blueprint[2][0] and b2 < m2 and b2 * t + r2 < m2 * t:
        p1 = dfs(r0 - blueprint[2][0] + b0, r1 - blueprint[2][1] + b1, r2 + b2, r3,
                 b0, b1, b2 + 1,
                 m0, m1, m2,
                 best_sofar, blueprint, minute)
    # build clay robot (b1)
    if r0 >= blueprint[1][0] and b1 < m1 and b1 * t + r1 < m1 * t:
        p2 = dfs(r0 - blueprint[1][0] + b0, r1 + b1, r2 + b2, r3,
                 b0, b1 + 1, b2,
                 m0, m1, m2,
                 best_sofar, blueprint, minute)
    # build ore robot (b0)
    if r0 >= blueprint[0][0] and b0 < m0 and b0 * t + r0 < m0 * t:
        p3 = dfs(r0 - blueprint[0][0] + b0, r1 + b1, r2 + b2, r3,
                 b0 + 1, b1, b2,
                 m0, m1, m2,
                 best_sofar, blueprint, minute)
    p4 = dfs(r0 + b0, r1 + b1, r2 + b2, r3,
             b0, b1, b2,
             m0, m1, m2,
             best_sofar, blueprint, minute)
    return max(p0, p1, p2, p3, p4)

ret = 1
for idx, blueprint in enumerate(BLUEPRINTS[:3]):
    idx += 1
    m0 = max([blueprint[_][0] for _ in range(4)])
    m1 = max([blueprint[_][1] for _ in range(4)])
    m2 = max([blueprint[_][2] for _ in range(4)])
    # print(m0, m1, m2)
    score = dfs(2, 0, 0, 0, 1, 0, 0, m0, m1, m2, 0, blueprint, 2)
    # print(score)
    ret *= score
    gc.collect()
print('part2', ret)
