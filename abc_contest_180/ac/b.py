n = int(input())
x_list = list(map(int, input().split()))

print(sum(abs(x) for x in x_list))
print(pow(sum(abs(x)**2 for x in x_list), 0.5))
print(max(abs(x) for x in x_list))
