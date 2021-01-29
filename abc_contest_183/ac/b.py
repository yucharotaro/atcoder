Sx, Sy, Gx, Gy = map(int, input().split())

a = (-Gy - Sy) / (Gx - Sx)
b = -a * Sx + Sy
x = -b/a
print(x)
