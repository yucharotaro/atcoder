N = int(input())
plans = [list(map(int, input().split())) for _ in range(N)]

now_x = 0
now_y = 0
now = 0
for t, x, y in plans:
    goal = abs(x - now_x + y - now_y)
    if goal > (t - now):
        print("No")
        exit()
    elif goal % (t - now) != 0:
        if ((t - now) - goal) % 2 != 0:
            print("No")
            exit()
    now = t
    now_x = x
    now_y = y
print("Yes")
