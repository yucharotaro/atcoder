d_x = [-1, 0, 1, 0]
d_y = [0, 1, 0, -1]


def dfs(H, W, C, seen, h, w):
    seen[h][w] = True

    for i in range(4):
        n_h = h + d_y[i]
        n_w = w + d_x[i]

        if n_h < 0 or n_h >= H or n_w < 0 or n_w >= W:
            continue
        if C[n_h][n_w] == "#":
            continue

        if seen[n_h][n_w]:
            continue

        dfs(H, W, C, seen, n_h, n_w)


def main():
    H, W = map(int, input().split())
    C = [list(list(input())) for _ in range(H)]
    seen = [[False] * W for _ in range(H)]
    s_h, s_w = 0, 0
    g_h, g_w = 0, 0
    for h in range(H):
        for w in range(W):
            if C[h][w] == "s":
                s_h, s_w = h, w
            if C[h][w] == "g":
                g_h, g_w = h, w

    dfs(H, W, C, seen, s_h, s_w)

    if seen[g_h][g_w]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
