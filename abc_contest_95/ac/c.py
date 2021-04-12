a, b, c, x, y = map(int, input().split())
ans = 0
if a + b > c * 2:
    ans = min(x, y) * (c * 2)
    tmp = max(x, y) * (c * 2)
    if x > y:
        ans += a * (x - y)
    else:
        ans += b * (y - x)
    ans = min(ans, tmp)
else:
    ans = a * x + b * y
print(ans)
