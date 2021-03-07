def f(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1


s = int(input())
a = [s]
for n in range(1, 10**6):
    target = f(a[n - 1])
    if target in a:
        print(n + 1)
        exit()
    a.append(target)
