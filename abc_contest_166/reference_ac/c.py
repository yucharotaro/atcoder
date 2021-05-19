N, M = map(int, input().split())
H = list(map(int, input().split()))

flag = [1] * N

for i in range(M):
    A, B = map(int, input().split())
    if (H[A - 1] < H[B - 1]):
        flag[A - 1] = 0
    elif (H[A - 1] > H[B - 1]):
        flag[B - 1] = 0
    else:
        flag[A - 1] = 0
        flag[B - 1] = 0

print(sum(flag))
