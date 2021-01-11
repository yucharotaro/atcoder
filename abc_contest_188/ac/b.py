from sys import stdin

n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += a_list[i] * b_list[i]

if ans == 0:
    print("Yes")
else:
    print("No")
