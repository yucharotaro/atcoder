N = int(input())
ans = -1
max_cnt = -1
for i in range(1, N + 1):
    cnt = 0
    tmp = i
    while tmp % 2 == 0:
        tmp //= 2
        cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        ans = i
print(ans)
