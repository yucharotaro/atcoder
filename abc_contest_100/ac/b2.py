D, N = map(int, input().split())

cnt = 0
target = 0
while cnt != N:
    if D == 0:
        target += 1
        if target % 100 != 0:
            cnt += 1
    if D == 1:
        target += 100
        if target % 10000 != 0:
            cnt += 1
    if D == 2:
        target += 10000
        if target % 1000000 != 0:
            cnt += 1

print(target)
