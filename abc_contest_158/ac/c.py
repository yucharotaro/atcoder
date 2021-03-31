from math import floor
a, b = map(int, input().split())

ans = []
i = 0
while True:
    if floor(i * 0.08) > a and floor(i * 0.1) > b:
        break
    if floor(i * 0.08) == a and floor(i * 0.1) == b:
        ans.append(i)
    i += 1
print(min(ans) if len(ans) > 0 else -1)
