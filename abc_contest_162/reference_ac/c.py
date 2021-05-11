k = int(input())
cnt = [0] * (k + 1)

for i in range(k, 0, -1):
    cnt[i] = (k // i)**3
    for j in range(i * 2, k + 1, i):
        cnt[i] -= cnt[j]

print(sum((i * cnt[i] for i in range(1, k + 1))))
