N = int(input())
S = input()
ans = 0
for i in range(N):
    X = set(list(S[:i]))
    Y = set(list(S[i:]))
    tmp = 0
    for x in X:
        if x in Y:
            tmp += 1
    ans = max(ans, tmp)
print(ans)
