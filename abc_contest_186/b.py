H, W = map(int, input().split())
a_lists = [list(map(int, input().split())) for _ in range(H)]
min_a = min(set(a for a_list in a_lists for a in a_list))
print(sum([a - min_a for a_list in a_lists for a in a_list]))
