N, X = map(int, input().split())
S = input()

for s in S:
    if s == "o":
        X += 1
    else:
        X -= 1
        X = max(X, 0)

print(X)
