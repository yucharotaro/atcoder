n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

print("Yes" if sum([a * b for a, b in zip(a_list, b_list)]) == 0 else "No")
