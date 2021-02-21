A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())

for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if b == A[i][j]:
                A[i][j] = 0

cnt = 0
for i in range(3):
    if A[0][i] == A[1][i] == A[2][i]:
        cnt += 1
    if A[i][0] == A[i][1] == A[i][2]:
        cnt += 1
if A[0][0] == A[1][1] == A[2][2]:
    cnt += 1
if A[0][2] == A[1][1] == A[2][0]:
    cnt += 1

print("Yes" if cnt >= 1 else "No")
