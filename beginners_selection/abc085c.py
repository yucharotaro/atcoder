N, Y = map(int, input().split())
x = y = z = -1

for a in range(N + 1):
    for b in range(N + 1 - a):
        c = N - a - b
        if (10000 * a + 5000 * b + 1000 * c) == Y:
            x = a
            y = b
            z = c
            break

print(x, y, z)
