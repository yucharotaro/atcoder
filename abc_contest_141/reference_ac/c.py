def main():
    n, k, q, *al = map(int, open(0).read().split())
    gl = [0] * n
    for a in al:
        gl[a - 1] += 1

    res = '\n'.join('Yes' if g > q - k else 'No' for g in gl)
    print(res)


if __name__ == '__main__':
    main()
