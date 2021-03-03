N = int(input())
v = sorted(list(map(int, input().split())))

value = (v[0] + v[1]) / 2
for i in range(2, N):
    value = (value + v[i]) / 2

print(value)
