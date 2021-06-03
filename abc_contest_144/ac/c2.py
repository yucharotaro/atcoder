def yakusu(x):
    ans = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            ans.append(i)
            ans.append(x // i)
    return ans


N = int(input())

y = yakusu(N)
print((y[-2] - 1) + (y[-1] - 1))
