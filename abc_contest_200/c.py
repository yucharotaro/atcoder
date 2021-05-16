N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    Ai = A[i]
    cnt += len([a for a in A[i + 1:] if (Ai - a) % 200 == 0])
print(cnt)
