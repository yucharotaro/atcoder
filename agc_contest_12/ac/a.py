n = int(input())
A = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    ans += A[-2 - (2 * i)]

print(ans)
