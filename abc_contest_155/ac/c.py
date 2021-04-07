n = int(input())

s_dict = {}
for _ in range(n):
    s = input()
    if s not in s_dict:
        s_dict[s] = 1
    else:
        s_dict[s] += 1
max_len = max(s_dict.values())
s_list = sorted([s[0] for s in s_dict.items() if s[1] == max_len])
for s in s_list:
    print(s)
