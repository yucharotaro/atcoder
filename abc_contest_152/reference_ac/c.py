def main():
    _ = int(input())
    min_num = 10**9
    ans = 0
    # ループ用の変数が配列にアクセスするだけなら
    # 配列そのものを回したほうが良い。
    for p in map(int, input().split()):
        if p < min_num:
            ans += 1
            min_num = p
    print(ans)


if __name__ == '__main__':
    # 関数の中で処理をした方が処理速度が早くなる。
    main()
