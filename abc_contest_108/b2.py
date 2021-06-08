x1, y1, x2, y2 = map(int, input().split())

# ベクトルを用いて考える。
# x1からx2に向かうベクトル座標を(dx, dy)とする。
dx = x2 - x1
dy = y2 - y1

# x2からx3、x3からx4に向かうベクトルの座標を求める。
for i in range(2):
    dx, dy = -dy, dx
    x2 += dx
    y2 += dy
    print(x2, y2, end=" ")
print()
