N = int(input())
W = [input() for i in range(N)]
if len(set(W)) != N:
    print("No")
    exit()
for i in range(1, N):
    if W[i - 1][-1] != W[i][0]:
        print("No")
        exit()
print("Yes")
