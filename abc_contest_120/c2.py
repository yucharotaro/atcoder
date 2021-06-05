S = input()

cnt = 0
before_len = len(S)
while True:
    S = S.replace("10", "")
    S = S.replace("01", "")

    if before_len == len(S):
        break
    cnt += before_len - len(S)
    before_len = len(S)

print(cnt)
