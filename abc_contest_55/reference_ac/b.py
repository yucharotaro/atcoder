def factorial(N):
    power_r = 1
    for n in range(2, N + 1):
        power_r = power_r * n % (10**9 + 7)
    return power_r


if __name__ == '__main__':
    N = int(input())
    print(factorial(N))
