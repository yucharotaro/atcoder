N, M = map(int, input().split())

min_id = 0
max_id = N + 1
for _ in range(M):
    L, R = map(int, input().split())
    if L > min_id:
        min_id = L

    if R < max_id:
        max_id = R

if max_id >= min_id:
    print(max_id - min_id + 1)
else:
    print(0)
