N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
X = list(map(int, input().split()))

for x in X:
    ans = x
    for a, t in A:
        if t == 1:
            ans += a
        elif t == 2:
            ans = max(ans, a)
        elif t == 3:
            ans = min(ans, a)
    print(ans)
