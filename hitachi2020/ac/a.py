s = input()
if len(s) % 2 != 0:
    print("No")
    exit()

i = 0
while i <= len(s) - 2:
    if s[i:i + 2] == "hi":
        i += 2
    else:
        print("No")
        exit()
print("Yes")
