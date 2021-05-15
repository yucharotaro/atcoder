from itertools import combinations, combinations_with_replacement

S = input()

o = 0
x = 0
q = 0
for s in S:
    if s == "o":
        o += 1
    elif s == "x":
        x += 1
    elif s == "?":
        q += 1

#print(f"o = {o}, x = {x}, q = {q}")
if o > 4:
    print(0)
    exit()

ans = 0
if o == 4:
    ans = len(list(combinations_with_replacement(range(4), 4)))
elif o == 0:
    nCr = len(list(combinations(range(q), 4)))
    ans = len(list(combinations_with_replacement(range(nCr), 4)))
else:
    ans = len(list(combinations_with_replacement(range(o + q), 4)))
print(ans)
