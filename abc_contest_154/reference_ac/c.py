n = input()
# 要素をint型に変換して受け取る必要はない
a = input().split(' ')
if len(set(a)) == n:
    print("YES")
else:
    print("NO")
