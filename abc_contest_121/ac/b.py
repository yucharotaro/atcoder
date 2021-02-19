import numpy as np

N, M, C = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
for _ in range(N):
    a = list(map(int, input().split()))
    if np.dot(a, b) + C > 0:
        ans += 1
print(ans)
