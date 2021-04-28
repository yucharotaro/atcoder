n = int(input())
a = list(input().split())
s = sum(int(i) for i in a)
m0 = 0
m1 = 0
c = 0
for i in a:
    m1 = m0
    m0 += int(i)
    if m0 * 2 == s:
        break
    elif m0 * 2 > s:
        c = min(m0 * 2 - s, s - m1 * 2)
        break

print(c)
