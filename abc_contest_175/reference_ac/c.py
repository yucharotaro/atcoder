x, k, d = map(int, input().split())
x = abs(x)
if x - d < 0:
    if k % 2 == 1:
        print(abs(x - d))
    else:
        print(x)
else:
    if x - k * d >= 0:
        print(x - k * d)
    else:
        num = x // d
        x = x - (num * d)
        k = k - num
        if k % 2 == 0:
            print(x)
        else:
            print(min(abs(x - d), abs(x + d)))
