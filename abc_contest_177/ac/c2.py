N = int(input())
A = list(map(int, input().split()))

sum_A = sum(A)
ans = 0
for i in range(N - 1):
    sum_A -= A[i]
    ans += sum_A * A[i]
print(ans % (10**9 + 7))
