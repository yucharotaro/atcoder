N, M = map(int, input().split())
H = list(map(int, input().split()))
peaks = [[] for _ in range(N)]
cnt = 0

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    peaks[A].append(B)
    peaks[B].append(A)

for i in range(N):
    flag = True
    for j in peaks[i]:
        if H[i] <= H[j]:
            flag = False
    if flag:
        cnt += 1

print(cnt)
