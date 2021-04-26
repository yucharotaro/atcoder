from itertools import permutations

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
total = 0
cnt = 0

for pair in permutations([e for e in range(n)]):
    cnt += 1
    pair = list(pair)
    for i in range(n - 1):
        total += ((xy[pair[i]][0] - xy[pair[i + 1]][0])**2 +
                  (xy[pair[i]][1] - xy[pair[i + 1]][1])**2)**0.5

print(total / cnt)
