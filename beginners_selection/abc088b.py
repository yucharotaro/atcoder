N = int(input())
a_list = map(int, input().split())
sorted_a_list = sorted(a_list)[::-1]

print(
    sum(n for i, n in enumerate(sorted_a_list) if i % 2 == 0) -
    sum(n for i, n in enumerate(sorted_a_list) if i % 2 != 0))
