s = input()
k = int(input())
a = 0
p = -1
for i in range(len(s)):
    if s[i] == "1":
        a += 1
    else:
        p = i
        break
if k <= a:
    print(1)
else:
    print(s[p])
