X = int(input())
M = int(input())

d = max(list(map(int, str(X))))
cnt = 0

n = d + 1
while True:
    tmp = 0
    for i, e in enumerate(str(X)[::-1]):
        tmp += int(e) * (n**i)
        if tmp > M:
            break
    if tmp <= M:
        cnt += 1
    else:
        break
    n += 1
print(cnt)
