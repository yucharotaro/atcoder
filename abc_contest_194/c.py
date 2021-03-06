N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += (N - 1) * pow(A[i], 2)
    # sum(A) は O(N) かかるので、このコードは最終的にO(N^2) かかる
    ans += -2 * A[i] * sum(A[i + 1:])
print(ans)
