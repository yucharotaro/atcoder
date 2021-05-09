S, P = map(int, input().split())

n, m = 1, S - 1
while True:
    if n * m > P:
        break

    if n * m == P:
        print("Yes")
        exit()

    n += 1
    m -= 1

print("No")
