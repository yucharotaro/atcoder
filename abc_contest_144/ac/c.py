N = int(input())
cnt = 0

ans = list()
i = 1
while i * i <= N:
    if N % i == 0:
        ans.append(i)
        ans.append(N // i)
    i += 1

goal_1 = ans[-2]
goal_2 = ans[-1]
cnt = abs(goal_1 - 1) + abs(goal_2 - 1)
print(cnt)
