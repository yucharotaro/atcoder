a, b, k = map(int, input().split())
ans = [i for i in range(a, a + k) if i > 0 and i <= b]
ans += [i for i in range(b - k + 1, b + 1) if i > 0 and i >= a]
ans = sorted(set(ans))
for e in ans:
    print(e)
