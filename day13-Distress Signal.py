from functools import cmp_to_key

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]
lines.append("")
A = []
ret = 0

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    if not isinstance(a, list):
        return compare([a], b)
    if not isinstance(b, list):
        return compare(a, [b])
    for i in range(min(len(a), len(b))):
        ret = compare(a[i], b[i])
        if ret != 0:
            return ret
    return compare(len(a), len(b))

i = 0
for line in lines:
    if line:
        i += 1
        A.append(eval(line))
B = [[2], [6]]
A.extend(B)
A.sort(key=cmp_to_key(compare))
ret = 1
for idx, a in enumerate(A):
    if a in B:
        ret *= idx + 1
print(ret)
