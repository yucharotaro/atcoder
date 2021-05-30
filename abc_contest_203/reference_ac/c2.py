def main():
    n, k = map(int, input().split())
    frends = {}

    for i in range(n):
        a, b = map(int, input().split())
        if a in frends.keys():
            frends[a] += b
        else:
            frends[a] = b

    keys = sorted(frends.keys())

    v = k
    for key in keys:
        if key <= v:
            v += frends[key]

    print(v)


if __name__ == "__main__":
    main()
