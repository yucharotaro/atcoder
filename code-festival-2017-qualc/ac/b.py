from functools import reduce

n = int(input())
a = list(map(int, input().split()))

total = 3**n
sal = [[e + 1, e, e - 1] for e in a]
odd = []
for sa in sal:
    cnt = 0
    for s in sa:
        if s % 2 == 1:
            cnt += 1
    odd.append(cnt)

print(total - reduce(lambda x, y: x * y, odd))
