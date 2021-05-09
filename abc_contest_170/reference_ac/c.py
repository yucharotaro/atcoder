import sys
readline = sys.stdin.readline

X, N = map(int, readline().split())
P = set(list(map(int, readline().split())))

x = X
while x in P:
    x -= 1
minX = x

x = X
while x in P:
    x += 1
maxX = x

if abs(minX - X) <= abs(maxX - X):
    print(minX)
else:
    print(maxX)
