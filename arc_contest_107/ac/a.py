A, B, C = map(int, input().split())
y = 998244353

sum_C = ((C * (1 + C)) // 2) % y
sum_B = ((B * sum_C * (1 + B)) // 2) % y
sum_A = ((A * sum_B * (1 + A)) // 2) % y
print(sum_A)
