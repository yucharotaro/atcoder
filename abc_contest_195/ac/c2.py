N = int(input())
cnt = 0
cmp = 1000000
c = 1
while N - cmp >= 0:
    cnt += c * (cmp - (cmp // 1000))
    c += 1
    cmp *= 1000

if N >= cmp // 1000:
    cnt += c * (N - cmp // 1000) + c

print(cnt)
