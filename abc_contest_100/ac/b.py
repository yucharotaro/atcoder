d, n = map(int, input().split())
ans = 0
for i in range(n):
    if i == 99:
        ans += 2 * (100**d)
    else:
        ans += 100**d
print(ans)
