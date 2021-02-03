n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
total = 0

for a, b in ab:
    total += (b - a + 1) * (a + b) / 2
print(int(total))
