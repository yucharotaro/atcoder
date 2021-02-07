S = input()
res = ""
for i in range(1 << 3):
    s = S[0:1]
    for j in range(3):
        s += list("+-")[i >> j & 1] + S[j + 1:j + 2]
    if eval(s) == 7:
        res = s
print(res, '=7')
