N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if i + 1 == A[A[i] - 1]:
        cnt += 1

print(cnt // 2)
