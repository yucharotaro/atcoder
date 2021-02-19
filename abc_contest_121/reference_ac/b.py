N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    tmp = C
    for j in range(M):
        tmp += A[i][j] * B[j]
    if tmp > 0:
        ans += 1

print(ans)
