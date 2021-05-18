import math


def calc_dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


A, B, H, M = map(int, input().split())

x1 = A * math.cos(math.radians((30 * H) + (0.5 * M)))
y1 = A * math.sin(math.radians((30 * H) + (0.5 * M)))
x2 = B * math.cos(math.radians(6 * M))
y2 = B * math.sin(math.radians(6 * M))
print(calc_dist(x1, y1, x2, y2))
