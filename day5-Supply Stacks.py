from collections import *
stacks = defaultdict(deque)
f = open('input')
l = ''
while '1' not in l:
    l = f.readline().replace('\n', '')
    for idx, char in enumerate(l):
        if char.isalpha():
            stacks[((idx - 1) >> 2) + 1].append(char)
f.readline()
for inst in f.readlines():
    inst = inst.replace('move ', '').replace(' from ', ' ').replace(' to ', ' ')
    n, start, end = (list(map(int, inst.split(' '))))
    i = 0
    items = []
    while i < n:
        items.append(stacks[start].popleft())
        i += 1
    for item in items[::-1]:
        stacks[end].appendleft(item)

ret = ''
for i in range(len(stacks)):
    ret += stacks[i+1][0]
print(ret)

