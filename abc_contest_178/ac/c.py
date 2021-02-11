n = int(input())
m = 10**9 + 7

ans = pow(10, n, m) - pow(9, n, m) - pow(9, n, m) + pow(8, n, m)
print(pow(ans, 1, m))
