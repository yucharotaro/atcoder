s = input()
if s[0] != "A":
    print("WA")
    exit(0)

c_cnt = 0
for ch in s[2:-1]:
    if ch == "C":
        c_cnt += 1

if c_cnt != 1:
    print("WA")
    exit(0)

s = s[1:]
s = s.replace("C", "")
if s.lower() != s:
    print("WA")
    exit(0)

print("AC")
