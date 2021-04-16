S = input()
N = int(S)

res = 0
for i in range(1, len(S)):
    if i % 2 == 1:
        res += 10**i - 10**(i - 1)

if len(S) % 2 == 1:
    res += N - 10**(len(S) - 1) + 1

print(res)
