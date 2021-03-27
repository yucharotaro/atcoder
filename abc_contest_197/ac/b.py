H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]
cnt = 0

for i in range(Y - 1, W):
    if S[X - 1][i] == ".":
        cnt += 1
    else:
        break

swp = 0
for i in range(0, Y - 1):
    if S[X - 1][i] == ".":
        swp += 1
    else:
        swp = 0
cnt += swp

for i in range(X - 1, H):
    if S[i][Y - 1] == ".":
        cnt += 1
    else:
        break

swp = 0
for i in range(0, X - 1):
    if S[i][Y - 1] == ".":
        swp += 1
    else:
        swp = 0
cnt += swp

print(cnt - 1 if cnt > 0 else 0)
