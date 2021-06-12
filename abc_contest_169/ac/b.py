N = int(input())
A = sorted(map(int, input().split()))

ans = 1
cmp = 10**18
for a in A:
    ans *= a
    if ans > cmp:
        print(-1)
        exit()
print(ans)
