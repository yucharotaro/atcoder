q, h, s, d = map(int, input().split())
n = int(input())
ans = 0
min_2l = min(q * 8, h * 4, s * 2, d)
min_1l = min(q * 4, h * 2, s)
if n > 1:
    ans = min_2l * (n // 2) + min_1l * (n % 2)
else:
    ans = min_1l
print(ans)
