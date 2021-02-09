N = int(input())
a_list = list(map(int, input().split()))
ans = 0
for i in range(N):
    min_count = a_list[i]
    for j in range(i, N):
        min_count = min(min_count, a_list[j])
        ans = max(ans, min_count * (j - i + 1))
print(ans)
