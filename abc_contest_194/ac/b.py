N = int(input())
task = [list(map(int, input().split())) for _ in range(N)]
A, B = list(map(list, zip(*task)))

minJobA = min(A)
minJobB = min(B)
taskA = A.index(minJobA)
taskB = B.index(minJobB)

if taskA == taskB:
    minJob = minJobA + minJobB
    for i in range(N):
        for j in range(N):
            if i != j:
                if minJob > max(A[i], B[j]):
                    minJob = max(A[i], B[j])
    print(minJob)

else:
    print(max(minJobA, minJobB))
