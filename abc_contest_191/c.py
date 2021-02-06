H, W = map(int, input().split())
s_lists = []
for _ in range(H):
    s_lists.append(list(input().split()))

tyoten = []
n = 0
for h in range(H):
    for s_list in s_lists[h]:
        for w in range(W):
            if s_list[w] == "#":
                tyoten.append((h, w))

for s in tyoten:
    tmp = 0
    if ((s[0] + 1, s[1]) not in tyoten):
        tmp += 1
    if ((s[0] - 1, s[1]) not in tyoten):
        tmp += 1
    if ((s[0], s[1] + 1) not in tyoten):
        tmp += 1
    if ((s[0], s[1] - 1) not in tyoten):
        tmp += 1
    if tmp > 1:
        n += 1
print(n)
