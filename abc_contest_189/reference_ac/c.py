N = int(input())
a_list = list(map(int, input().split()))
ans = 0
for l in range(N):
    x = 10 ** 6
    for r in range(l, N):
        x = min(x, a_list[r])
        ans = max(ans, x * (r - l + 1))
print(ans)
