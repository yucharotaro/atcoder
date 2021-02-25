N, M = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))[::-1]
total_A = sum(A)

for i in range(M):
    if (4 * A[i] * M < total_A):
        print("No")
        exit()
print("Yes")
