from itertools import combinations
N = int(input())
L = list(map(int, input().split()))
ans = 0

for pair in combinations(L, 3):
    if len(set(pair)) != 3:
        continue
    b, c, a = sorted(pair)
    if abs(b - c) < a < b + c:
        ans += 1
print(ans)
