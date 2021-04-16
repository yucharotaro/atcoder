n = int(input())
H = list(map(int, input().split()))

before = H[0]
for i in range(1, n):
    if H[i] > before:
        H[i] -= 1
        before = H[i]
    elif before > H[i]:
        print("No")
        exit()

print("Yes")
