from pprint import pprint
import bisect

lines = open('input').readlines()
lines = [_.strip() for _ in lines]
cycles = [20]
for n in range(5):
    cycles.append(cycles[-1] + 40)
print(cycles)
slow = 0
fast = 0
x = 1
ops = dict()
for line in lines:
    if line == 'noop':
        fast += 1
    else:
        num = int(line[5:])
        fast += 2
        ops[fast] = num
    slow += 1
ret = 0
prev = 0
for i in range(1, 221):
    if i in ops:
        x += ops[i]
    if i in cycles:
        ret += i * prev
    prev = x
pprint(ret)
