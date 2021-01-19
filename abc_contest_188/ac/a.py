from sys import stdin

x, y = map(int, input().split())

team_point_low = min(x, y)
team_point_up = max(x, y)

if (team_point_up - team_point_low) < 3:
    print("Yes")
else:
    print("No")
