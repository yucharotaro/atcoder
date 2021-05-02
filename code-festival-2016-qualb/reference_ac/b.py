import sys


def main():
    n, a, b = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().rstrip()

    ans = ["No"] * n
    success = 0
    foreigner = 0

    for i in range(n):
        if s[i] == "a":
            ans[i] = "Yes"
            success += 1
        elif s[i] == "b" and foreigner < b:
            ans[i] = "Yes"
            success += 1
            foreigner += 1
        if success == a + b:
            break

    print("\n".join(ans))
    return


if __name__ == "__main__":
    main()
