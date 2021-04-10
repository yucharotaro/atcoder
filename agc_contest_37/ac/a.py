S = input()
cnt = 1
pre_word = S[0]
now = ""
for i in range(1, len(S)):
    now += S[i]
    if pre_word != now:
        cnt += 1
        pre_word = now
        now = ""
print(cnt)
