S = input()
set_S = set(S)
if len(set_S) == 26:
    print("None")
else:
    sorted_S = sorted(list(set_S))
    asciicode = 97
    for i in range(len(sorted_S)):
        if ord(sorted_S[i]) != asciicode:
            print(chr(asciicode))
            exit()
        asciicode += 1
    print(chr(asciicode))
