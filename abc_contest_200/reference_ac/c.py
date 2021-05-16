N = int(input())
A = map(int, input().split())

k = [0] * 200
for a in A:
    k[a % 200] += 1

cnt = 0
for x in k:
    cnt += (x * (x - 1)) // 2

print(cnt)
