N = int(input())
XY = [list(map(int, input().split())) for i in range(N)]
ans = 0
for x1, y1 in XY:
    for x2, y2 in XY:
        ans += ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(ans / N)
