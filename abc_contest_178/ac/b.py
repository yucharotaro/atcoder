a, b, c, d = list(map(int, input().split()))
ans = -float("INF")
for x in [a, b]:
    for y in [c, d]:
        if ans < x * y:
            ans = x * y
print(ans)
