n = int(input())
a_list = list(map(int, input().split()))
gcd = 0
ans = 0
for i in range(2, max(a_list) + 1):
    tmp = sum(a % i == 0 for a in a_list)
    if (gcd < tmp):
        gcd = tmp
        ans = i
print(ans)
