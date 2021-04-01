N = int(input())
t, a = map(int, input().split())
H = list(map(int, input().split()))

cmp = abs(a - (t - H[0] * 0.006))
ans = 1
for i in range(1, N):
    tmp = abs(a - (t - H[i] * 0.006))
    if min(cmp, tmp) == tmp:
        cmp = tmp
        ans = i + 1

print(ans)
