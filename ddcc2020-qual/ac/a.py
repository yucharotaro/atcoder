x, y = map(int, input().split())

ans = 0
for e in (x, y):
    if e == 1:
        ans += 300000
    elif e == 2:
        ans += 200000
    elif e == 3:
        ans += 100000

if ans == 600000:
    ans += 400000

print(ans)
