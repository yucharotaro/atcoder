def check(S):
    dep = 0
    for s in S:
        if s == "(":
            dep += 1
        else:
            dep -= 1

        if dep < 0:
            return False

    if dep == 0:
        return True
    else:
        return False


def main():
    N = int(input())

    for i in range(2**(N - 1)):
        s = ""
        for j in reversed(range(N)):
            #print(f"i = {i}, j = {j} i >> j = {i >> j}")
            if (i >> j) & 1:
                s += ")"
            else:
                s += "("

        if check(s):
            print(s)


if __name__ == "__main__":
    main()
