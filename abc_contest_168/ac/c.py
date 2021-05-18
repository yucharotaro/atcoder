import math

A, B, H, M = map(int, input().split())

c = 2 * math.pi * 1 * ((H / 12 + (M / 60) / 12) - (M / 60))
print((A**2 + B**2 - (2 * A * B * math.cos(c)))**0.5)
