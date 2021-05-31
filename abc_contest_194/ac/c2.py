N = int(input())
A = list(map(int, input().split()))

sum_A = sum(A)
double = sum(map(lambda x: x * x, A))

tmp = 0
for a in A:
    sum_A -= a
    tmp += a * sum_A

print((N - 1) * double - 2 * tmp)
