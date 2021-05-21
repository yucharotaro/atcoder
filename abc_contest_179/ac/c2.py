def bin_search(a, N):
    left = -1
    right = N + 1
    while right - left > 1:
        b = (left + right) // 2
        if a * b >= N:
            right = (left + right) // 2
        else:
            left = (left + right) // 2
    return left


def main():
    N = int(input())
    pair = 0

    for a in range(1, N):
        if a > N:
            break
        b = bin_search(a, N)
        pair += b
    print(pair)


if __name__ == "__main__":
    main()
