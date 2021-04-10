def main():
    S = input().rstrip()
    ans, prev, cur = 0, "", ""
    for s in S:
        cur += s
        if cur != prev:
            ans += 1
            prev, cur = cur, ""
    print(ans)


if __name__ == "__main__":
    main()
