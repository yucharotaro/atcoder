N = int(input())

cmp = 1
cnt = 0
while int(str(cmp) + str(cmp)) <= N:
    cnt += 1
    cmp += 1
print(cnt)
