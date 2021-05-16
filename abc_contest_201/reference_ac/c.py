S = input()
ans = 0
for i in range(10000):
    T = f"{i:04d}"
    ok = True
    for j in range(10):
        if S[j] == "?":
            continue
        elif S[j] == "o":
            if str(j) not in T:
                ok = False
        elif S[j] == "x":
            if str(j) in T:
                ok = False
    if ok:
        ans += 1
print(ans)
