X, N = map(int, input().split())
P = list(map(int, input().split()))

if N == 0:
    print(X)
    exit()

plus = X
minus = X
while True:
    ans = []
    if plus not in P:
        ans.append(plus)
    if minus not in P:
        ans.append(minus)
    if len(ans) > 0:
        print(min(ans))
        exit()

    plus += 1
    minus -= 1
