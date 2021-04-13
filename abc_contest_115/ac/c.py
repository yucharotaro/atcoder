n, k = map(int, input().split())
tree = sorted([int(input()) for _ in range(n)])
ans = float("INF")
for i in range(n - k + 1):
    if tree[i + k - 1] - tree[i] < ans:
        ans = tree[i + k - 1] - tree[i]
print(ans)
