from itertools import combinations
n = int(input())
xy_tuples = [tuple(map(int, input().split())) for _ in range(n)]

for pair in combinations(xy_tuples, 3):
    a, b, c = pair
    if (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1]):
        print("Yes")
        exit()
print("No")
