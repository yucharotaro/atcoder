N = int(input())
A = list(map(int, input().split()))

ans = 0
cnt = 0
for a in A:
    if a > 10:
        ans += a
        cnt += 1
print(ans - cnt * 10)
