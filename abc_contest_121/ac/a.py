H, W = map(int, input().split())
h, w = map(int, input().split())

total_white = H * W
total_white -= (h * W)
total_white -= (w * (H - h))
print(total_white)
