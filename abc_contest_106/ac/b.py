n = int(input())
ans = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        tmp = []
        for j in range(1, i):
            if i % j == 0:
                tmp.append(i // j)
                tmp.append(j)
        if len(set(tmp)) == 8:
            ans += 1

print(ans)
