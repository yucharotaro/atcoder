N, x = map(int, input().split())
sorted_A = sorted(list(map(int, input().split())))

if sum(sorted_A) == x:
    print(N)
elif min(sorted_A) > x:
    print(0)
else:
    cnt = 0
    for i in range(N):
        if i < N - 1:
            if x >= sorted_A[i]:
                x -= sorted_A[i]
                cnt += 1
            else:
                break
        if i == N - 1:
            if x == sorted_A[i]:
                cnt += 1
    print(cnt)
