def main():
    _ = int(input())
    H = map(int, input().split())
    min_h = 0
    ret = True
    for h in H:
        if min_h > h:
            ret = False
            break
        min_h = max(min_h, h - 1)
    print('Yes' if ret else 'No')


main()
