n = int(input())
a = list(map(int, input().split()))
cnt = 0
chk = 1
for i in range(len(a)):
    if chk != a[i]:
        cnt += 1
    else:
        chk += 1
print(cnt if chk != 1 else -1)
