n, s, d = map(int, input().split())
spels = [list(map(int, input().split())) for _ in range(n)]

for spel in spels:
    if (spel[0] < s and spel[1] > d):
        print("Yes")
        exit()
print("No")
