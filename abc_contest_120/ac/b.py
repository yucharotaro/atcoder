def f(x):
    ans = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            ans.append(i)
            ans.append(x // i)
    return sorted(ans)


a, b, k = map(int, input().split())
ans = sorted(list(set(f(a)) & set(f(b))), reverse=True)[k - 1]
print(ans)
