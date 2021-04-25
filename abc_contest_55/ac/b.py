n = int(input())
power = 1

for i in range(1, n + 1):
    power = pow(power * i, 1, 10**9 + 7)

print(power)
