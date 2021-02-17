n = int(input())
xxx = list(map(int, input().split()))
ans = 10**10
for p in range(1, 101):
    tmp = sum((x - p)**2 for x in xxx)
    ans = min(ans, tmp)
print(ans)
