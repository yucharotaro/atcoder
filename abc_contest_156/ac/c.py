n = int(input())
x = sorted(list(map(int, input().split())))
ans = float("INF")
for i in range(min(x), max(x) + 1):
    tmp = 0
    for e in x:
        tmp += (e - i)**2
    ans = min(ans, tmp)
print(ans)
