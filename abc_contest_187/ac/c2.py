N = int(input())
S = set([input() for _ in range(N)])

for s in S:
    if "!" in s:
        if s[1:] in S:
            print(s[1:])
            exit()
    else:
        if "!" + s in S:
            print(s)
            exit()

print("satisfiable")
