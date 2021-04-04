def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)


A, B = map(int, input().split())
print(A * B // gcd(A, B))
