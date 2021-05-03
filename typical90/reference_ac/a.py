def cut_yokan(M):
    global N
    global L
    global K

    cnt = 0
    pre = 0
    for i in range(N):
        if A[i] - pre >= M and L - A[i] >= M:
            cnt += 1
            pre = A[i]
            #print(f"A[i] = {A[i]}, cnt = {cnt}")

    if cnt >= K:
        return True
    else:
        return False


N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

left = 0
right = L
while right - left > 1:
    mid = (left + right) // 2
    #print(f"left = {left}, right = {right}, mid = {mid}")
    if cut_yokan(mid):
        left = mid
    else:
        right = mid

print(left)
