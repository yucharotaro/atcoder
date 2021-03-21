N = int(input())
P = list(map(int, input().split()))

min_p = P[0]
cnt = 1
for i in range(1, N):
    if min_p >= P[i]:
        min_p = P[i]
        cnt += 1
print(cnt)
