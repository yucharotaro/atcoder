from math import factorial
from itertools import permutations


def calc_dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


N = int(input())
V = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for pair in permutations(range(N), N):
    for i in range(N - 1):
        ans += calc_dist(
            V[pair[i]][0],
            V[pair[i]][1],
            V[pair[i + 1]][0],
            V[pair[i + 1]][1],
        )

print(ans / factorial(N))
