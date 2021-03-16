def main():
    A, B, C, X = [int(input()) for _ in [0] * 4]

    cnt = 0
    for i in range(A + 1):
        for j in range(B + 1):
            n = i * 500 + j * 100
            if n == X:
                cnt += 1
            elif n < X:
                if X - n <= C * 50:
                    cnt += 1
    print(cnt)


main()
