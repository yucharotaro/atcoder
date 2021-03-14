s = input()
ans = 10**3 + 1
for i in range(len(s) - 2):
    cmp = abs(753 - int(s[i:i + 3]))
    if ans > cmp:
        ans = cmp
print(ans)
