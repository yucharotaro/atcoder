N, K, Q = map(int, input().split())
points = [K - Q for _ in range(N)]

for i in range(Q):
    a = int(input())
    points[a - 1] += 1

for point in points:
    print("Yes" if point > 0 else "No")
