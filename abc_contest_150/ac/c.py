from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

i = 0
a = b = 0
for pair in permutations(range(1, N + 1), N):
    i += 1
    if pair == P:
        a = i
    if pair == Q:
        b = i

print(abs(a - b))
