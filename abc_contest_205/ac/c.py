A, B, C = map(int, input().split())

if C % 2 == 0:
    if abs(A) == abs(B):
        print("=")
    elif abs(A) < abs(B):
        print("<")
    elif abs(A) > abs(B):
        print(">")
else:
    if A == B:
        print("=")
    elif A < 0 and B < 0:
        if abs(A) < abs(B):
            print(">")
        elif abs(A) > abs(B):
            print("<")
    elif A >= 0 and B >= 0:
        if A > B:
            print(">")
        elif A < B:
            print("<")
    elif A >= 0 and B < 0:
        print(">")
    elif A < 0 and B >= 0:
        print("<")
