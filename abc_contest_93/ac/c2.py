N = sorted(list(map(int, input().split())))

cnt = 0
while len(set(N)) != 1:
    if N[1] != N[2]:
        t = N[2] - N[1]
        N[0] += t
        N[1] += t
        cnt += t
    elif N[1] == N[2]:
        if (N[2] - N[0]) % 2 == 0:
            cnt += (N[2] - N[0]) // 2
            N[0] += N[2] - N[0]
        else:
            N[0] += 2
            N[1] += 1
            N[2] += 1
            cnt += 2
    N = sorted(N)
print(cnt)
