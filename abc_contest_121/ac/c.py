N, M = map(int, input().split())
drinks = sorted([list(map(int,
                          input().split())) for _ in range(N)],
                key=lambda x: x[0])

cnt = 0
ans = 0
for a, b in drinks:
    if cnt == M:
        break

    if b > M - cnt:
        ans += a * (M - cnt)
        cnt += M - cnt
    else:
        ans += a * b
        cnt += b

print(ans)
