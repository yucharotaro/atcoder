N = int(input())
a_list = list(map(int, input().split()))
ans = 0
for left in range(N):
    for right in range(left, N):
        # 範囲が広く、TLEとなる。
        min_count = min(a_list[left:right + 1])
        ans = max(ans, min_count * (right - left + 1))
print(ans)
