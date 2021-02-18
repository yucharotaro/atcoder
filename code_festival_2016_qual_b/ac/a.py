s = input()
c = "CODEFESTIVAL2016"
ans = 0
for i in range(len(s)):
    if s[i] != c[i]:
        ans += 1
print(ans)
