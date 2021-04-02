s = input()
t = input()
for i in range(1, len(s) + 1):
    s = s[-1] + s[:-1]
    if s == t:
        print("Yes")
        exit()
print("No")
