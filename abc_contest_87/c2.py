N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

cnt = A1[0] + A2[-1]
sum_A1 = sum(A1) - A1[0]
sum_A2 = sum(A2) - A2[-1]
for i in range(N - 1):
    if sum_A1 > sum_A2:
        cnt += A1[i + 1]
    else:
        cnt += sum_A2
        break
    sum_A1 -= A1[i + 1]
    sum_A2 -= A2[i]

print(cnt)
