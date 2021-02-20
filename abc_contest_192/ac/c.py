def g1(x):
    x_list = list(map(str, str(x)))
    x_list = sorted(x_list, reverse=True)
    sorted_x = int("".join(x_list))
    return sorted_x


def g2(x):
    x_list = list(map(str, str(x)))
    x_list = sorted(x_list)
    sorted_x = int("".join(x_list))
    return sorted_x


def f(x):
    return g1(x) - g2(x)


N, K = list(map(int, input().split()))
ai = N
for _ in range(K):
    ai = f(ai)
print(ai)
