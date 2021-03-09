N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

choco = X
for a in A:
    day = 0
    while True:
        if day * a + 1 <= D:
            choco += 1
            day += 1
        else:
            break

print(choco)
