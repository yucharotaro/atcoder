S = input()

a = 0
b = 0
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == "1":
            a += 1
        else:
            b += 1
    else:
        if S[i] == "0":
            a += 1
        else:
            b += 1
print(min(a, b))
