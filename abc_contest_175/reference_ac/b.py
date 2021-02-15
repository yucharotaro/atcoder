N = int(input())
L = list(map(int, input().split()))
cnt = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if len(set([
                    L[i], L[j], L[k]
            ])) == 3 and 2 * max([L[i], L[j], L[k]]) < sum([L[i], L[j], L[k]]):
                cnt += 1
print(cnt)
