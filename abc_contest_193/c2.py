N = int(input())

cnt = 0
for i in range(2, N):
    for j in range(2, N):
        if i**j > N:
            break
        print(i**j)
        cnt += 1
    print(f"cnt={cnt}")

print(N - cnt)
