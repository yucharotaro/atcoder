N = int(input())
T = list(map(int, input().split()))
M = int(input())
D = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    p, x = D[i]
    total = 0
    for j in range(N):
        if j + 1 == p:
            total += x
        else:
            total += T[j]
    print(total)
