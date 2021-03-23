N, K, X, Y = [int(input()) for _ in range(4)]

if N <= K:
    print(N * X)
else:
    print(K * X + (N - K) * Y)
