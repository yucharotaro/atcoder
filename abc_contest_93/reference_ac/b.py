a, b, k = map(int, input().split())
if a + k >= b - k + 1:
    s = list(range(a, b + 1))
else:
    s = list(range(a, a + k)) + list(range(b - k + 1, b + 1))
for i in s:
    print(i)
