N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))

left = list(range(1, X))
right = list(range(X + 1, N))

print(min(len(set(A) & set(right)), len(set(A) & set(left))))
