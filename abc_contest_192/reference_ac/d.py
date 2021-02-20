def f(x, d):
    x = str(x)[::-1]
    a = p = 0
    for i in x:
        a += (int(i) % d) * d**p
        p += 1
    return a


x = input()
m = int(input())
d = max(int(i) for i in x)
l, r = d, 10**60 + 10
while r - l > 1:
    c = (l + r) // 2
    if m >= f(x, c):
        l = c
    else:
        r = c
print(l - d if l < 10**60 else 1)
