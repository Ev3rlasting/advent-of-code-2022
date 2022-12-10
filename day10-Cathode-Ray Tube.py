lines = open('input').readlines()
lines = [_.strip() for _ in lines]
cycles = [1]
for n in range(6):
    cycles.append(cycles[-1] + 40)
pending = 0
x = 1
ops = dict()
for line in lines:
    if line == 'noop':
        pending += 1
    else:
        num = int(line[5:])
        pending += 2
        ops[pending] = num
ret = []
for i in range(1, 242):
    if i in cycles:
        print(''.join(ret))
        ret.clear()
    if (i - 1) % 40 in [x - 1, x, x + 1]:
        ret.append('#')
    else:
        ret.append('.')
    if i in ops:
        x += ops[i]
