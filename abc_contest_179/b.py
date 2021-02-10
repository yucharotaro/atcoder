n = int(input())
d_lists = [list(map(int, input().split())) for _ in range(n)]

for i in range(2, n):
    if d_lists[i - 2][0] == d_lists[i - 2][1] \
       and d_lists[i - 1][0] == d_lists[i - 1][1] \
       and d_lists[i][0] == d_lists[i][1]:
        print("Yes")
        exit()
print("No")
