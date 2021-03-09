a, b, c, d = [int(input()) for _ in range(4)]

total = 0
if a > b:
    total += b
else:
    total += a

if c > d:
    total += d
else:
    total += c

print(total)
