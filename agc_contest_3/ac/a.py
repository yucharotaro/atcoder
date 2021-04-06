S = input()

if "N" in S and "S" in S:
    if "E" in S and "W" in S:
        print("Yes")
        exit()
    elif "E" not in S and "W" not in S:
        print("Yes")
        exit()
elif "N" not in S and "S" not in S:
    if "E" in S and "W" in S:
        print("Yes")
        exit()

print("No")
