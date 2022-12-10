from collections import Counter

for line in open('input').readlines():
    line = line.strip()
    start = 0
    c = Counter(line[:4])
    while start <= len(line) - 4:
        if len(c) == 4:
            print(start + 4)
            break
        c[line[start]] -= 1
        if c[line[start]] == 0:
            del c[line[start]]
        c[line[start + 4]] = c.get(line[start + 4], 0) + 1
        start += 1
