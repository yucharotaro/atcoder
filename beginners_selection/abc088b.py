N = int(input())
a_list = map(int, input().split())
sorted_a_list = sorted(a_list)[::-1]

print(sum(sorted_a_list[::2]) - sum(sorted_a_list[1::2]))
