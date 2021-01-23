N = int(input())
d_list = [int(input()) for _ in range(N)]
sorted_uniq_d_list = sorted(list(set(d_list)))[::-1]

print(len(sorted_uniq_d_list))
