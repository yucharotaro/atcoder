N, M = map(int, input().split())
c = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    c[a - 1] += 1
    c[b - 1] += 1

# 出力のためにループ回すなら
# アンパックしてsepで改行したほうが早いし、メモリも節約可。
print(*c, sep='\n')
