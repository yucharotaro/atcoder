N, M = map(int, input().split())
drinks = [list(map(int, input().split())) for _ in range(N)]

drinks.sort(key=lambda x: x[0])
m = 0
i = 0
while M > 0:
    if drinks[i][1] > M:
        m += drinks[i][0] * M
        M = 0
    else:
        m += drinks[i][0] * drinks[i][1]
        M -= drinks[i][1]
        i += 1
print(m)
