from itertools import product
n = int(input())
count = 0
n_e = [e for e in range(1, n)]
for pair in product(n_e, repeat=3):
    a, b, c = pair
    if a * b + c == n:
        count += 1
print(count)
