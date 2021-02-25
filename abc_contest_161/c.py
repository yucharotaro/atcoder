N, K = map(int, input().split())

left = 0
right = (N // K) + 1
while abs(left - right) > 1:
    mid = left + right // 2
    if N >= K * mid:
        left = mid
    else:
        right = mid
print(min(abs(N - K * left), abs(N - K * right)))
