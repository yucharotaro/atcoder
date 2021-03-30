n, d = map(int, input().split())
ps = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        s = 0
        for x1, x2 in zip(ps[i], ps[j]):
            s += (x1 - x2)**2
        s = s**0.5
        if s == int(s):
            cnt += 1
print(cnt)
