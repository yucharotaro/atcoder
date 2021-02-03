N = int(input())
s_sum = 0

# リストに入れて順に処理していくより、
# 逐次処理したほうがメモリ消費を抑えられる
for i in range(N):
    A, B = map(int, input().split())
    s_sum += (B - A + 1) * (A + B) / 2

print(int(s_sum))
