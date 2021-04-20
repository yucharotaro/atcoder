n = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
ans = A[0].pop(0)
ans += A[1].pop()
candies = 0

for i in range(n - 1):
    candies = max(candies, sum(A[0][:i]) + sum(A[1][i:]))

print(ans + candies)
