def R():
    return map(int, input().split())


input()
a = list(R())
r = y = 0
for u, v, w in zip(R(), a, a[1:]):
    x = min(v - y, u)
    y = min(w, u - x)
    r += x + y
print(r)
