n = int(input())
a = [int(i) for i in input().split()]
c = [0] * 2
for i in a:
    c[i % 2] += 1
print(3**n - 2**c[0])
