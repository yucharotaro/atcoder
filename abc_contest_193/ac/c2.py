N = int(input())

ans = []
for i in range(2, N):
    if i**2 > N:
        break
    for j in range(2, N):
        if i**j > N:
            break
        ans.append(i**j)

ans = list(set(ans))
print(N - len(ans))
