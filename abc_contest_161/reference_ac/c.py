n, k = map(int, input().split())
t = n % k

print(min(t, k - t))
