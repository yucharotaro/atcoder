from math import ceil

r, x, y = map(int, input().split())
d = (x**2 + y**2)**(1 / 2)
if r > d:
    print(ceil(d / r) + 1)
else:
    print(ceil(d / r))
