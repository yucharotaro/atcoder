A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

price = min(a) + min(b)
for _ in range(M):
    x, y, c = map(int, input().split())
    tmp = a[x - 1] + b[y - 1] - c
    if price > tmp:
        price = tmp

print(price)
