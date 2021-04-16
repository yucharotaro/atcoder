n = int(input())
cnt = 0
cmp = 9
base = 1

while cmp < n:
    cnt += cmp - base + 1
    cmp = int(str(cmp) + "99")
    base = int(str(base) + "00")
if n >= base:
    cnt += n - base + 1

print(cnt)
