H, W = map(int, input().split())
S = [list(list(input())) for i in range(H)]

ans = 0
for i in range(H - 1):
    for j in range(W - 1):
        print(i, j)
        count = (S[i][j] == '#') * 1 + (S[i + 1][j] == '#') * 1 + (
            S[i][j + 1] == '#') * 1 + (S[i + 1][j + 1] == '#') * 1
        if count == 1 or count == 3:
            ans += 1

print(ans)
