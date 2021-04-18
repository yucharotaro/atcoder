n, a, b = map(int, input().split())

if b - a > 1:
    print((b - a) // 2)
else:
    if a - 1 < n - b:
        print(b - 1)
    else:
        print(n - a)
