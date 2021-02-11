n = int(input())
ans = 0

# aを固定するとbは約数の対象性から一意に決まる。
# そのとき式は、aの倍数 + c = n
# aの倍数を1つ決めるとc = n - (aの倍数)と一意に決まる。
# つまり、n - 1以下の整数からaの倍数を数えれば良い。
for i in range(1, n):
    ans += (n - 1) // i
print(ans)
