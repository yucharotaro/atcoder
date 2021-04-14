n, k, m = map(int, input().split())
A = list(map(int, input().split()))
s = n * m - sum(A)
if s > k:
    print(-1)
elif s < 0:
    print(0)
else:
    print(s)
