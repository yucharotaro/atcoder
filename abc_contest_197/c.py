N = int(input())
A = list(map(int, input().split()))

ans = 2**30 + 1
if N == 1:
    ans = A[0]

for i in range(1, N):
    pre_A = A[0:i]
    after_A = A[i:N]
    a = pre_A[0]
    b = after_A[0]

    if len(pre_A) != 1:
        for i in range(1, len(pre_A)):
            a |= pre_A[i]

    if len(after_A) != 1:
        for i in range(1, len(after_A)):
            b |= after_A[i]

    ans = min(ans, a ^ b)

print(ans)
