N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = [0 for _ in range(N)]
for j in range(N):
    ans[B[C[j] - 1] - 1] += 1

cnt = 0
for i in range(N):
    cnt += ans[A[i - 1] - 1]
print(cnt)
