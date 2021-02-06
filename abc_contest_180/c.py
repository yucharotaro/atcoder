n = int(input())
mod = 1000000007

for i in range(n):
    if (n % mod) % (i + 1) == 0:
        print(i + 1)
