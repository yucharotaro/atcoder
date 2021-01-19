n = int(input())
a = list(map(int, input().split()))

l = max(a[:2**n // 2])
r = max(a[2**n // 2:])

if l > r:
    print(a.index(r) + 1)
else:
    print(a.index(l) + 1)
