N, X = map(int, input().split())
alc = 0
for i in range(N):
    v, p = map(int, input().split())
    alc += v * p
    if (alc > 100 * X):
        print(i + 1)
        exit()

print(-1)
