N = int(input())
A = list(map(int, input().split()))
A = [(A[i], i + 1) for i in range(N)]
A = sorted(A)
A = [A[i][1] for i in range(N)]
print(*A)
