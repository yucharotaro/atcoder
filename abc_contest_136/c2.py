N = int(input())
H = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    print(H[i - 1], H[i])
    if H[i - 1] + 1 > H[i]:
        print("No")
        exit()
    else:
        H[i - 1] -= 1

print("Yes")
