N = int(input())
A = [int(input()) for _ in range(N)]

i = 0
cnt = 0
while True:
    cnt += 1
    i = A[i] - 1
    if A[i] == 2:
        print(cnt + 1)
        exit()
    if cnt >= N:
        break
print(-1)
