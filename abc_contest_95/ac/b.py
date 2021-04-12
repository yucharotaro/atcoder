n, x = map(int, input().split())
D = sorted([int(input()) for _ in range(n)])
x -= sum(D)
print(n + x // D[0])
