n, _ = map(int, input().split())
a = sorted([input() for _ in [0] * n])
print(*a, sep='')
