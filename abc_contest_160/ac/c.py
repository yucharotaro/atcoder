K, N = list(map(int, input().split()))
A = list(map(int, input().split()))
cost = K - abs(A[0] - A[-1])

for i in range(N - 1):
    tmp_cost = abs(A[i + 1] - A[i])
    if (cost < tmp_cost):
        cost = tmp_cost
print(K - cost)
