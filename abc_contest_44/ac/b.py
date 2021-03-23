w = input()
set_w = set(w)

for sw in set_w:
    if w.count(sw) % 2 != 0:
        print("No")
        exit()
print("Yes")
