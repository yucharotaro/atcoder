x1, y1, x2, y2 = map(int, input().split())
x3 = y3 = x4 = y4 = 0

d = (x2 - x1)**2 + (y2 - y1)**2
x3 = x2 - d if x2 <= 0 else x2 + d
y3 = y2 + d if y2 <= 0 else y2 - d
print(x3, y3, x4, y4)
