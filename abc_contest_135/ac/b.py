n = int(input())
p_list = list(map(int, input().split()))
sorted_p_list = sorted(p_list)

d = 0
for sp, p in zip(sorted_p_list, p_list):
    if sp != p:
        d += 1

print("YES" if d <= 2 else "NO")
