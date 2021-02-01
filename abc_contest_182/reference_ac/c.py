from itertools import product

S = input()
A = [int(x) for x in S]

k = len(S)
ans = k

for bits in product((True, False), repeat=k):
    digit_sum = 0
    score = 0
    for i, bit in enumerate(bits):
        if bit:
            digit_sum += A[i]
        else:
            score += 1

    if digit_sum % 3 == 0:
        ans = min(ans, score)

if ans == k:
    print(-1)
else:
    print(ans)
