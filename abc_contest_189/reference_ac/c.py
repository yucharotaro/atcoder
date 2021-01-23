N = int(input())
a_list = list(map(int, input().split()))
ans = 0
for left in range(N):
    x = a_list[left]
    for right in range(left, N):
        x = min(x, a_list[right])
        ans = max(ans, x * (right - left + 1))
print(ans)
