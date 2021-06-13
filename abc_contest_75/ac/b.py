H, W = map(int, input().split())
S = [list(map(str, list(input()))) for _ in range(H)]
T = [["" for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            b = []

            if j - 1 >= 0:
                b.append(S[i][j - 1])
            if j + 1 < W:
                b.append(S[i][j + 1])

            if i - 1 >= 0:
                b.append(S[i - 1][j])
                if j - 1 >= 0:
                    b.append(S[i - 1][j - 1])
                if j + 1 < W:
                    b.append(S[i - 1][j + 1])

            if i + 1 < H:
                b.append(S[i + 1][j])
                if j - 1 >= 0:
                    b.append(S[i + 1][j - 1])
                if j + 1 < W:
                    b.append(S[i + 1][j + 1])
            T[i][j] = str(b.count("#"))
        else:
            T[i][j] = "#"

for i in range(H):
    print("".join(T[i]))
