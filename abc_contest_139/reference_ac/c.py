import sys
input = sys.stdin.readline


def main():

    _ = int(input())
    ls_H = list(map(int, input().split()))

    max_, tmp = 0, 0
    for i, j in zip(ls_H[:-1], ls_H[1:]):
        if i >= j:
            tmp += 1
            if max_ < tmp:
                max_ = tmp
        else:
            tmp = 0
    print(max_)


if __name__ == "__main__":
    main()
