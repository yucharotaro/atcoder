N = int(input())
max_T = [0, 0]
max_S = ["", ""]
for _ in range(N):
    S, T = input().split()
    T = int(T)
    if T > max_T[-1]:
        max_T[-1], max_T[-2] = T, max_T[-1]
        max_S[-1], max_S[-2] = S, max_S[-1]
    elif T > max_T[-2]:
        max_T[-2] = T
        max_S[-2] = S
print(max_S[-2])
