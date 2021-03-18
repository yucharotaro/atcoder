S = input()
odd_S = S[::2]
even_S = S[1::2]

if "L" not in odd_S and "R" not in even_S:
    print("Yes")
else:
    print("No")
