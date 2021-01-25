n = int(input())
x_y_lists = [list(map(int, input().split())) for _ in range(n)]
pair = 0

for i in range(len(x_y_lists)):
    xi = x_y_lists[i][0]
    yi = x_y_lists[i][1]
    for j in range(i + 1, len(x_y_lists)):
        xj = x_y_lists[j][0]
        yj = x_y_lists[j][1]
        if -1 <= (yj - yi) / (xj - xi) <= 1:
            pair += 1

print(pair)
