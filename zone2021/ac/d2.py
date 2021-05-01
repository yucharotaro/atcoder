def main():
    S = input()
    T = ""

    rFlag = False
    for s in S:
        if s == "R":
            rFlag = not rFlag
        else:
            if rFlag:
                T = s + T
            else:
                T = T + s
        if len(T) >= 2:
            if T[0] == T[1]:
                T = T[2:]
            elif T[-1] == T[-2]:
                T = T[:-2]

    T = T[::-1] if rFlag else T

    print(T)


main()
