def f(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


s = int(input())
ans = 1
# setを使用するとin演算子はO(1)で済む。
# ちなみにlistの場合のin演算子はO(n)かかる。
# listからsetへの変換が必要な場合は時間がかかり
# 返って遅くなる場合があるため、初めからsetを使用すべき。
used = set()
while True:
    if s in used:
        break

    used.add(s)
    ans += 1
    s = f(s)
print(ans)
