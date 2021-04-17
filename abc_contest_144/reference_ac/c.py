N = int(input())
n = int(N**0.5)
while True:
    if N % n == 0:
        break
    n -= 1
print(n + N // n - 2)
