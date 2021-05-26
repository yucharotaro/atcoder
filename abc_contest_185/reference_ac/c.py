from math import factorial
L = int(input())

# 区切りを置く場所に注目して組み合わせ
# 端以外から、11個の区切りを置く場所の組み合わせを考える。
# n = L - 1としたときのnC11
ans = factorial(L - 1) // (factorial(L - 1 - 11) * factorial(11))
print(ans)
