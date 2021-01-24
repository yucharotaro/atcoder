N = int(input())
txy_lists = [list(map(int, input().split())) for _ in range(N)]

dt = dx = dy = 0
for t, x, y in txy_lists:
    if (any([
            abs(x - dx) + abs(y - dy) == (t - dt),
            abs(x - dx) + abs(y - dy) == (t - dt) % 2
    ])):
        dx = x
        dy = y
        dt = t
    else:
        print("No")
        exit()
print("Yes")
