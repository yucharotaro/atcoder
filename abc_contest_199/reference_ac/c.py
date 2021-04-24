N = int(input())
S = input()
Q = int(input())

X = [[], []]
X[0] = list(S[:N])  # first half
X[1] = list(S[N:])  # second half

for _ in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        X[a // N][a % N], X[b // N][b % N] = X[b // N][b % N], X[a // N][a % N]
    if t == 2:
        X[0], X[1] = X[1], X[0]
    print(X)

print("".join(X[0] + X[1]))
