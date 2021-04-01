S = input()

if S[0] != "A":
    print("WA")
    exit()

index_C = -1
if S[2:-1].count("C") != 1:
    print("WA")
    exit()
else:
    index_C = S[2:-1].index("C") + 2

for i in range(len(S)):
    if i != 0 and i != index_C:
        if S[i].lower() != S[i]:
            print("WA")
            exit()

print("AC")
