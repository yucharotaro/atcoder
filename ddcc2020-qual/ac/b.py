n = int(input())
a = list(map(int, input().split()))

sum_a = sum(a)
m = 2020202020
step = 0
for i in range(n):
    step += a[i]
    sum_a -= a[i]
    m = min(m, abs(step - sum_a))
print(m)
