a, b, w = map(int, input().split())

min_c = 10**6 + 1
max_c = 0

for i in range(1, 10**6 + 1):
    if a * i <= 10**3 * w and 10**3 * w <= b * i:
        # print(i, a * i, b * i)
        min_c = min(min_c, i)
        max_c = max(max_c, i)

if max_c == 0:
    print("UNSATIFIABLE")
else:
    print(min_c, max_c)
