def is_AGCT(c):
    if c in ("A", "G", "C", "T"):
        return True
    else:
        return False


S = input()
len_S = len(S)

cnt = 0
tmp = 0
for i in range(len_S):
    if is_AGCT(S[i]):
        tmp += 1
    else:
        cnt = max(cnt, tmp)
        tmp = 0
print(max(cnt, tmp))
