def main():
    _ = input()
    a = list(map(int, input().split()))
    max_height = 0
    ans = 0
    for height in a:
        if max_height <= height:
            max_height = height
        else:
            ans += max_height - height
    print(ans)


if __name__ == "__main__":
    main()
