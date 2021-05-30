n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()

now = k
for a, b in ab:
    if a <= now:
        now += b

print(now)
