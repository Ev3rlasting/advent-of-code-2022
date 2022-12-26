f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]
total = 0
for line in lines:
    n = 0
    for ch in line:
        n *= 5
        n += int(ch) if ch.isnumeric() else -" -=".index(ch)
    total += n
print('total', total)

ret = ''
while total:
    total, m = divmod(total, 5)
    if m <= 2:
        ret += str(m)
    else:
        ret += "   =-"[m]
        total += 1
print(ret[::-1])
