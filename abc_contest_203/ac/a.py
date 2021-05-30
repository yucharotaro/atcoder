A, B, C = map(int, input().split())

if A == B == C:
    print(A)
    exit()

if len(set([A, B, C])) == 2:
    if A == B:
        print(C)
    elif B == C:
        print(A)
    elif A == C:
        print(B)
else:
    print(0)
