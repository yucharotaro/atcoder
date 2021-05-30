N, K = map(int, input().split())

ans = 0
for n in range(N):
    for k in range(K):
        ans += int(str(n + 1) + "0" + str(k + 1))
print(ans)
