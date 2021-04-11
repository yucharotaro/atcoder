N = input()
cnt = 0
for i in range(len(N)):
    cnt += int(N[i])

a = int(N[0])
# -1することでNの各位の総数-1を実現できる
a += (len(N) - 1) * 9 - 1
a = max(a, cnt)

print(a)
