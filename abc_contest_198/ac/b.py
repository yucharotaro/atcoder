N = input()

if N == N[::-1]:
    print("Yes")
else:
    after = ""
    for i in range(1, len(N)):
        if N[-i] == "0":
            after += "0"
        else:
            break
    new_N = after + N
    if new_N == new_N[::-1]:
        print("Yes")
    else:
        print("No")
