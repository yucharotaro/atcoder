from itertools import product

L = int(input())
L -= 12

cnt = 0
# このコードは当然ながらTLE。
for pair in product(range(L + 1), repeat=12):
    if sum(pair) == L:
        cnt += 1

print(cnt)
