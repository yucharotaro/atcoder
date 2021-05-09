A, B, C = map(int, input().split())
_sum = A * (A + 1) // 2 * B * (B + 1) // 2 * C * (C + 1) // 2
print(_sum % 998244353)
