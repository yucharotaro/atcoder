N, M = map(int, input().split())
R = set(range(1, M + 1))
for _ in range(N):
    K, *A = map(int, input().split())
    R &= set(A)
print(len(R))
