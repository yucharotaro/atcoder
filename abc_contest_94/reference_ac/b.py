_, m, *a = map(int, open(0).read().split())
c = sorted(a).index(a[0])
print(min(c, m - c))
