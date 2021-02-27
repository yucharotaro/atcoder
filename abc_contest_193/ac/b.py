N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]

now = 0
buy = 10**9 + 1
for i in range(N):
    now += m[i][0] - now
    if (m[i][2] - now) > 0:
        if buy > m[i][1]:
            buy = m[i][1]
print(buy if buy != 10**9 + 1 else -1)
