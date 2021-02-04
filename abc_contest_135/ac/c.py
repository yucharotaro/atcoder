n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

m = 0
for i in range(n):
    m += min(b_list[i], a_list[i])
    p = b_list[i] - a_list[i]
    if p > 0:
        m += min(p, a_list[i + 1])
        a_list[i + 1] -= min(p, a_list[i + 1])
print(m)
