N, M = map(int, input().split())
H = list(map(int, input().split()))
peaks = [True for _ in range(N)]
cnt = N

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    if H[A] > H[B]:
        if peaks[B]:
            peaks[B] = False
            cnt -= 1
    elif H[B] > H[A]:
        if peaks[A]:
            peaks[A] = False
            cnt -= 1
    elif H[A] == H[B]:
        if peaks[A]:
            peaks[A] = False
            cnt -= 1
        if peaks[B]:
            peaks[B] = False
            cnt -= 1

print(cnt)
