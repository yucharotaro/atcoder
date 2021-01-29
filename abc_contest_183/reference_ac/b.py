sx, sy, gx, gy = map(float, input().split())
# SxからGxへの変化をSy:Gyに内分する座標を求める
print((sx * gy + gx * sy) / (sy + gy))
