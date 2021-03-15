A, B = map(int, input().split())
S = input()

if not S[:A].isdigit() or not S[B + 1:].isdigit() or S[A] != "-":
    print("No")
else:
    print("Yes")
