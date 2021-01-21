n = int(input())
a_list = list(map(int, input().split()))
ans = 0

while True:
    if (len(list(filter(lambda x: x % 2 != 0, a_list)))) > 0:
        break
    a_list = list(x / 2 for x in a_list)
    ans += 1

print(ans)
