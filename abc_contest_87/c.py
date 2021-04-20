n = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
#candies = A[0][0] + A[1][n - 1]
candies = 0
i, j = 0, 0

while i != 1 and j != n - 1:
    if A[i + 1][j] > A[i][j + 1]:
        i += 1
    else:
        j += 1

print(candies)
