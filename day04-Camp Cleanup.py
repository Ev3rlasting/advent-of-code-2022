a = []
for line in open('input').readlines():
    a.append(line.strip())
ret = 0
for line in a:
    g1, g2 = line.split(',')
    l = sorted([list(map(int, g1.split('-'))), list(map(int, g2.split('-')))])
    ret += l[1][0] <= l[0][1]
print(ret)
