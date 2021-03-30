N, D = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        dist = 0
        for d in range(D):
            dist += (x[j][d] - x[i][d])**2
        if (dist**0.5).is_integer():
            cnt += 1

print(cnt)
