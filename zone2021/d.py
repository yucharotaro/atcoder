def main():
    S = input()
    #S = "abc" * 2 * (10**5)
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
    T = T[::-1] if rFlag else T

    N = [e * 2 for e in list("abcdefghijklmnopqrstuvwxyz")]
    while True:
        before_T = T
        for n in N:
            T = T.replace(n, "")
        if T == before_T:
            break

    print(T)


main()
