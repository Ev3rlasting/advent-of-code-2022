a = []
for line in open('input').readlines():
    a.append(line.strip())
ret = 0
n = 0
g = []
for line in a:
    g.append(line)
    n += 1
    if n == 3:
        ch = set(g[0]).intersection(set(g[1])).intersection(set(g[2])).pop()
        if ch.islower():
            ret += ord(ch) - 96
        else:
            ret += ord(ch) - 38
        g.clear()
        n = 0
print(ret)