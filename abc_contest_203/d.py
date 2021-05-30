N, K = map(int, input().split())
t = int(K**2 // 2) + 1
print(t)

A = [list(map(int, input().split())) for _ in range(N)]

D = N - K
li = []
for d in range(D + 1):
    S = []
    for i in range(d, N - d):
        for j in range(d, N - d):
            S.append(A[i][j])
    li.append(S[t - 1])
print(min(li))
