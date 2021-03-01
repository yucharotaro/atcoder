S = input()
set_S = set(S)
if len(set_S) == 2:
    for e in set_S:
        if S.count(e) != 2:
            print("No")
            exit()
    print("Yes")
else:
    print("No")
