a, b = map(int, input().split())
sum_a = sum(map(int, str(a)))
sum_b = sum(map(int, str(b)))
print(sum_a if sum_a > sum_b else sum_b)
