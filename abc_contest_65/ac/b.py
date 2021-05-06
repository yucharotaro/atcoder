N = int(input())
A = [int(input()) for _ in range(N)]

i = 0
cnt = 0
while True:
    if A[i] == 2:
        print(cnt + 1)
        exit()
    if cnt >= N:
        print(-1)
        exit()

    cnt += 1
    i = A[i] - 1
