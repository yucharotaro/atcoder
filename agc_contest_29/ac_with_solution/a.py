S = input()

cnt = 0
cnt_b = 0
for s in S:
    if s == "B":
        cnt_b += 1
    else:
        cnt += cnt_b

print(cnt)
