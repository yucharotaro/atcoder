N = int(input())
A = [int(input()) for _ in range(N)]

sorted_A = sorted(A)
max_A = sorted_A[-1]
second_A = sorted_A[-2]
for i in range(N):
    if A[i] != max_A:
        print(max_A)
    else:
        print(second_A)
