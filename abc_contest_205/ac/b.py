N = int(input())
A = list(map(int, input().split()))

for n in range(N):
    if A.count(n + 1) != 1:
        print("No")
        exit()

print("Yes")
